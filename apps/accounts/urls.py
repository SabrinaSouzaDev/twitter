from django.urls import path
from .views import (
    SwaggerAutoLoginView,
    UserCreateView,
    UserDetailView,
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    # # UserProfileView
)

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('profile/', UserDetailView.as_view(), name='profile'),
    path('login-swagger/', SwaggerAutoLoginView.as_view(), name='login-swagger'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]
