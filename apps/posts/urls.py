from django.urls import path
from apps.posts.views import PostCreateView, PostViewSet, PostSearchView, LikePostView, UnlikePostView

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('', PostViewSet.as_view(), name='post-list'),
    path('search/', PostSearchView.as_view(), name='post-search'),  # Nova rota de busca
    path('<int:post_id>/like/', LikePostView.as_view(), name='post-like'),
    path('<int:post_id>/unlike/', UnlikePostView.as_view(), name='post-unlike'),
]
