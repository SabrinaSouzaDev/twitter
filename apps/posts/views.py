from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.posts.models import Post, PostLike
from apps.posts.serializers import PostSerializer
from apps.follows.models import Follow
from django.core.cache import cache

class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostViewSet(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        cache_key = f"user_feed_{user.pk}"
        cached = cache.get(cache_key)

        if cached is not None:
            return cached

        followed_ids = Follow.objects.filter(follower=user).values_list('followed_id', flat=True)
        queryset = Post.objects.filter(author__id__in=followed_ids).select_related('author').prefetch_related('likes')
        cache.set(cache_key, queryset, 120)  # cache de 2 minutos
        return queryset


class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = generics.get_object_or_404(Post, id=post_id)
        PostLike.objects.get_or_create(post=post, user=request.user)
        return Response({'detail': 'Post curtido com sucesso.'}, status=status.HTTP_200_OK)


class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = generics.get_object_or_404(Post, id=post_id)
        PostLike.objects.filter(post=post, user=request.user).delete()
        return Response({'detail': 'Curtida removida com sucesso.'}, status=status.HTTP_200_OK)
