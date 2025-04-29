"""
URL configuration for mini_twitter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin 
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.accounts.views import CustomTokenObtainPairView, UserCreateView, UserDetailView
from apps.follows.views import FollowView
from apps.posts.views import PostViewSet


router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Autenticação
    path('apps/auth/register/', UserCreateView.as_view(), name='register'),
    path('apps/auth/login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('apps/auth/me/', UserDetailView.as_view(), name='me'),
    
    # Relacionamentos
    path('apps/follow/', FollowView.as_view(), name='follow'),
    # path('apps/follow/<int:pk>/', FollowView.as_view({'delete'}), name='unfollow'),
    
    # Posts (via Router)
    path('apps/', include(router.urls)),
]