from django.shortcuts import render

from django.core.cache import cache
from rest_framework import generics, permissions
from posts.models import Post
from posts.serializers import PostSerializer
from django.db.models import Q

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        cache_key = f'user_feed_{user.id}'
        queryset = cache.get(cache_key)

        if queryset is None:
            following_ids = user.following.values_list('followed_id', flat=True)
            queryset = Post.objects.filter(
                Q(author__id__in=following_ids) | Q(author=user)
            ).order_by('-created_at')
            cache.set(cache_key, queryset, timeout=60 * 5)  # Cache for 5 minutes

        return queryset
