from rest_framework.viewsets import ModelViewSet # type: ignore
from rest_framework.decorators import api_view, permission_classes # type: ignore
from rest_framework.permissions import AllowAny, IsAuthenticated # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework.generics import CreateAPIView # type: ignore
from rest_framework.authtoken.models import Token # type: ignore

from django.contrib.auth.models import User # type: ignore
from django.contrib.auth import authenticate, login # type: ignore
from django.http import JsonResponse # type: ignore
from django.views.decorators.csrf import csrf_exempt # type: ignore
from django.conf import settings # type: ignore
import json, requests # type: ignore
#from .telegram_bot import send_message
from django.views.decorators.csrf import csrf_exempt # type: ignore
from django.http import JsonResponse # type: ignore
import json
from rest_framework.views import APIView # type: ignore
from .models import  TelegramMessage
from .utils import send_message # type: ignore

from .models import Task
from .serializer import TaskSerializer, UserSerializer
from .tasks import test_func, send_welcome_email

# ✅ Task API
class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# ✅ Public API
@api_view(['GET'])
@permission_classes([AllowAny])
def public_api(request):
    return Response({"message": "This is a public endpoint, no auth needed."})

# 🔐 Protected API
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_api(request):
    return Response({"message": f"Hello {request.user.username}, you are authenticated."})

# ✅ Celery Test Endpoint
@api_view(['GET'])
@permission_classes([AllowAny])
def test_celery_view(request):
    test_func.delay()
    return Response({"message": "Celery task has been triggered."})

# ✅ Send Email via Celery
@api_view(['GET'])
@permission_classes([AllowAny])
def send_email_view(request):
    send_welcome_email.delay()
    return Response({"message": "📧 Welcome email task triggered!"})

# ✅ Auth - Registration
class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

# ✅ Auth - Login
@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})
    return Response({"error": "Invalid Credentials"}, status=400)

# ✅ Auth - Profile
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    return Response({"username": request.user.username})

# ✅ Telegram Bot Message Sender
def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

# ✅ Telegram Webhook Handler


@csrf_exempt
def telegram_webhook(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        message = data.get('message', {})
        chat = message.get('chat', {})
        text = message.get('text', '')
        chat_id = chat.get('id')
        username = chat.get('username')
        first_name = chat.get('first_name')

        if chat_id:
            # ✅ Save new message to DB
            TelegramMessage.objects.create(
                chat_id=chat_id,
                username=username,
                first_name=first_name,
                message_text=text
            )

        if text == "/start":
            TelegramUser.objects.get_or_create( # type: ignore
                chat_id=chat_id,
                defaults={
                    'username': username,
                    'first_name': first_name
                }
            )
            send_message(chat_id, f"👋 Welcome {first_name or username}! You’ve been registered.")
        return JsonResponse({"status": "ok"})
    return JsonResponse({"error": "invalid method"}, status=405)



@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, World!"})


class TelegramMessagesAPIView(APIView):
    def get(self, request):
        messages = TelegramMessage.objects.all().values()
        return Response(list(messages))