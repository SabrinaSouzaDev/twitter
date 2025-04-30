from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from apps.accounts.models import User
from apps.accounts.serializers import UserSerializer
from apps.follows.models import Follow
from apps.follows.serializers import FollowSerializer


class FollowView(generics.CreateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Follow.objects.all()
    def get_serializer_class(self):
        return FollowSerializer

    def create(self, request, *args, **kwargs):
        followed_id = request.data.get('user_id')
        followed = get_object_or_404(User, pk=followed_id)
        
        if request.user == followed:
            return Response(
                 {"error": "Você não pode seguir a si mesmo."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        follow, created = Follow.objects.get_or_create(
            follower=request.user,
            followed=followed
        )
        
        if not created:
            return Response(
              {"error": "Você já está seguindo esse usuário."},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = FollowSerializer(follow)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        follow = get_object_or_404(
            Follow,
            follower=request.user,
            followed_id=kwargs['pk']
        )
        follow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FollowingListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(
            followers__follower=self.request.user
        )

class FollowersListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(
            following__followed=self.request.user
        )