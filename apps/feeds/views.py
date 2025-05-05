from django.core.cache import cache
from rest_framework import generics
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated

from apps.posts.models import Post
from apps.posts.serializers import PostSerializer


class FeedView(generics.ListAPIView):
    """
    View para exibir o feed de posts do usuário, incluindo os posts do próprio
    usuário e dos usuários que ele segue, com caching para performance.
    """
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        cache_key = f"user_feed_{user.pk}"
        post_ids = cache.get(cache_key)

        if post_ids is None:
            following_ids = user.following.values_list('followed_id', flat=True)  # type: ignore
            queryset = Post.objects.filter(
                Q(author__in=following_ids) | Q(author=user)
            ).order_by('-created_at')

            post_ids = list(queryset.values_list('id', flat=True))
            cache.set(cache_key, post_ids, timeout=60 * 5)  # Cache por 5 minutos

        return Post.objects.filter(id__in=post_ids).order_by('-created_at')
