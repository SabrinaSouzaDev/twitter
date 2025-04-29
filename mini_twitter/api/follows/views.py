from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Follow
from .serializers import FollowSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

class FollowAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Se um usuário tentar seguir a si mesmo, retornamos um erro
        if request.data['follower'] == request.data['following']:
            return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        # Verificamos se a relação de follow já existe
        follower = request.user
        following = User.objects.get(id=request.data['following'])
        
        if Follow.objects.filter(follower=follower, following=following).exists():
            return Response({"error": "You are already following this user."}, status=status.HTTP_400_BAD_REQUEST)

        # Criamos a nova relação de follow
        follow = Follow.objects.create(follower=follower, following=following)
        serializer = FollowSerializer(follow)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        # Deixa de seguir um usuário
        follower = request.user
        following = User.objects.get(id=request.data['following'])

        try:
            follow = Follow.objects.get(follower=follower, following=following)
        except Follow.DoesNotExist:
            return Response({"error": "You are not following this user."}, status=status.HTTP_400_BAD_REQUEST)

        follow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
