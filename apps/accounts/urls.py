from django.urls import path
from apps.accounts.views import (
    CustomTokenObtainPairView, 
    CustomTokenRefreshView,
    UserCreateView, 
    UserDetailView,
)

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('me/', UserDetailView.as_view(), name='user-detail'),
]
