from django.urls import path
from apps.posts.views import (
    PostCreateView, PostViewSet, LikePostView, UnlikePostView
)

urlpatterns = [
    path('', PostViewSet.as_view(), name='feed'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('<int:post_id>/like/', LikePostView.as_view(), name='like-post'),
    path('<int:post_id>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
]
