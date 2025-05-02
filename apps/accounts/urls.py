from django.urls import path
from apps.accounts.views import (
    CustomTokenObtainPairView, 
    CustomTokenRefreshView,
    UserCreateView, 
    UserDetailView, 
    UserProfileView
)

urlpatterns = [
    # Endpoint para registrar um novo usuário
    path('register/', UserCreateView.as_view(), name='register'),

    # Endpoint para obter detalhes do perfil do usuário logado (GET) ou atualizá-lo (PUT)
    path('me/', UserDetailView.as_view(), name='user-detail'),

    # Endpoint para login (obter o token JWT)
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Endpoint para refresh do token JWT
    path('api/accounts/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),

    # Endpoint para acessar ou editar o perfil do usuário logado
    path('profile/', UserProfileView.as_view(), name='user_profile'),
]
