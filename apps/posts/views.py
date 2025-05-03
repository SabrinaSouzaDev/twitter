from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.posts.models import Post, PostLike
from apps.posts.serializers import PostSerializer
from mini_twitter.pagination import StandardResultsSetPagination


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related('author').all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
    # def send_email_to_followed_user(email, post_id):
    #     print(f"Enviando email para {email} sobre o post {post_id}")
    
    @action(detail=True, methods=['post', 'delete'])
    def like(self, request, pk=None):
        post = self.get_object()

        if request.method == 'POST':
            like, created = PostLike.objects.get_or_create(
                post=post,
                user=request.user
            )
            if not created:
                return Response(
                    {'error': 'Post already liked'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            return Response({
                'status': 'liked',
                'like_count': post.like_count  # Retorna o número de curtidas após a ação
            }, status=status.HTTP_201_CREATED)

        elif request.method == 'DELETE':
            try:
                like = PostLike.objects.get(post=post, user=request.user)
                like.delete()
                return Response({
                    'status': 'unliked',
                    'like_count': post.like_count  # Retorna o número de curtidas após a ação
                }, status=status.HTTP_204_NO_CONTENT)
            except PostLike.DoesNotExist:
                return Response(
                    {'error': 'Post not liked'},
                    status=status.HTTP_404_NOT_FOUND
                )
