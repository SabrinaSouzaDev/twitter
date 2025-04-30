from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.posts.views import PostViewSet


# Criação de um router e registro do viewset
router = DefaultRouter()
router.register(r'posts', PostViewSet)

# Incluindo as URLs do router
urlpatterns = [
    path('', include(router.urls)),  # Registra todas as URLs do viewset
]
