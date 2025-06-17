from django.urls import path # type: ignore
from . import views
from .views import TelegramMessagesAPIView 
urlpatterns = [
    path('hello/', views.hello_world, name='hello'),
    path('profile/', views.get_profile, name='profile'),
    path('test/', views.test_celery_view, name='test_celery'),
    path('send-email/', views.send_email_view, name='send_email'),
    path('telegram-webhook/', views.telegram_webhook, name='telegram_webhook'),
    path('messages/', TelegramMessagesAPIView.as_view(), name='messages'),


]



