from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from apps.accounts.views import CustomTokenObtainPairView, UserCreateView, UserDetailView
from apps.follows.views import FollowView
from apps.posts.views import PostViewSet

# Configurando o roteador para o PostViewSet
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

# Definindo o schema para a documentação
schema_view = get_schema_view(
    openapi.Info(
        title="Mini Twitter API",
        default_version='v1',
        description="Documentação da API do projeto Mini Twitter. API de seguidores, usuários e autenticação JWT",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@minitwitter.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),  # Permite que qualquer pessoa visualize a documentação
)

urlpatterns = [
    path('admin/', admin.site.urls),  # Página do admin
    path('', include(router.urls)),  # URLs para os posts via router
    
    # Autenticação e contas
    path('apps/auth/register/', UserCreateView.as_view(), name='register'),
    path('apps/auth/login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('apps/auth/me/', UserDetailView.as_view(), name='me'),
    # Feed
    # Follows
    path('follows/', include('apps.follows.urls')),
    # swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
     
]
