from django.urls import path
from .views import (

    LogoutView,
    UserCreateView,
    UserDetailView,
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    UserProfileView,
)

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('me/', UserDetailView.as_view(), name='user-detail'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]
