
from django.urls import path

from apps.accounts import views
# from apps.accounts.views import CustomTokenObtainPairView, UserCreateView, UserDetailView


urlpatterns = [
    # path('register/', UserCreateView.as_view(), name='register'),
    # path('me/', UserDetailView.as_view(), name='user-detail'),
    # path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('profile/', views.UserProfileView.as_view(), name='user_profile'),
]
