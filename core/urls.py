from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from rest_framework.routers import DefaultRouter # type: ignore
from MyAPI.views import TaskViewSet
from rest_framework.authtoken.views import obtain_auth_token # type: ignore
from rest_framework_simplejwt.views import ( # type: ignore
    TokenObtainPairView,
    TokenRefreshView,
)

# Create router for viewsets
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # DRF router URLs (e.g. /api/tasks/)
    path('api/', include(router.urls)),

    # DRF TokenAuth (optional)
    path('api/token-auth/', obtain_auth_token, name='token_auth'),

    # JWT Auth endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Django's built-in login/logout views (if needed for browsable API login)
    path('accounts/', include('django.contrib.auth.urls')),

    # Custom API URLs from your app (api/urls.py)
    path('api/custom/', include('MyAPI.urls')),
    
]
