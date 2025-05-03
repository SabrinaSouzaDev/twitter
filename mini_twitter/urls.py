from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from apps.posts.views import PostViewSet



def index(request):
    return render(request, 'index.html')


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
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    # URL para a documentação da API
    path('api/v1/', include([
        path('', include(router.urls)),
            # Posts
        path('posts/', include('apps.posts.urls')),
            # Autenticação
        path('accounts/', include('apps.accounts.urls')),
            # Feeds
        path('feeds/', include('apps.feeds.urls')),
            # Follows
        path('follows/', include('apps.follows.urls')),
    ])),
    # Swagger UI (documentação da API)
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
]