from django.core.cache import cache
from rest_framework import generics
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated

from apps.feeds.serializers import FeedPostSerializer
from apps.posts.models import Post
from rest_framework.pagination import PageNumberPagination
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class FeedPagination(PageNumberPagination):
    page_size = 10

class UserFeedView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FeedPostSerializer
    pagination_class = FeedPagination
    
    @method_decorator(cache_page(60 * 15))  # Cache por 15 minutos
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

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
