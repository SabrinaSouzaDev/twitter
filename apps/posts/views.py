from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.request import Request
from typing import cast


from apps.posts.models import Post, PostLike
from apps.posts.serializers import PostSerializer
from mini_twitter.pagination import StandardResultsSetPagination


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related('author').all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        request = cast(Request, self.request)
        search = request.query_params.get('search')
        queryset = Post.objects.select_related('author').all()
        if search:
            queryset = queryset.filter(
                Q(content__icontains=search) |
                Q(content__icontains=f'#{search}')
            )
        return queryset

    def perform_create(self, serializer):
        # Atribui o usuário autenticado como autor
        serializer.save(author=self.request.user)

    def get_serializer_context(self):
        # Permite que o serializer tenha acesso ao request (para is_liked)
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

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
                'like_count': post.like_count
            }, status=status.HTTP_201_CREATED)

        elif request.method == 'DELETE':
            try:
                like = PostLike.objects.get(post=post, user=request.user)
                like.delete()
                return Response({
                    'status': 'unliked',
                    'like_count': post.like_count
                }, status=status.HTTP_204_NO_CONTENT)
            except PostLike.DoesNotExist:
                return Response(
                    {'error': 'Post not liked'},
                    status=status.HTTP_404_NOT_FOUND
                )