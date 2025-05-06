
from django.contrib import admin
from django.urls import path, include
from apps.feeds.urls import urlpatterns as feeds_urls
from apps.posts.urls import urlpatterns as posts_urls
from rest_framework.routers import DefaultRouter

from apps.posts.views import PostViewSet

from mini_twitter.docs.schema import schema_view

# Roteador da API
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')


urlpatterns = [
    path('admin/', admin.site.urls),
      # API V1
      path('api/v1/', include([
          path('posts/', include(posts_urls)),  # /api/v1/posts/ (list, create, like/unlike)
          path('auth/', include('apps.accounts.urls')),  # CASE 1: auth endpoints
          path('follows/', include('apps.follows.urls')),  # CASE 3: follow/unfollow
          path('feeds/', include(feeds_urls)),  # CASE 4: viewing feed
      ])),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
]
