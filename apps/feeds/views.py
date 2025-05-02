from django.core.cache import cache
from rest_framework import generics, permissions
from apps.posts.models import Post
from django.db.models import Q

from apps.posts.serializers import PostSerializer

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        cache_key = f'user_feed_{user.id}'
        post_ids = cache.get(cache_key)

        if post_ids is None:
            following_ids = user.following.values_list('followed_id', flat=True)
            queryset = Post.objects.filter(
                Q(author__id__in=following_ids) | Q(author=user)
            ).order_by('-created_at')
            
            post_ids = list(queryset.values_list('id', flat=True))
            cache.set(cache_key, post_ids, timeout=60 * 5)

        return Post.objects.filter(id__in=post_ids).order_by('-created_at')
