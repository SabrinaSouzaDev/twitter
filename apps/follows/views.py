from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from apps.follows.models import Follow
from apps.follows.serializers import FollowSerializer
from django.core.mail import send_mail

from celery import shared_task


# Função Celery para envio de e-mail quando alguém segue outro
@shared_task
def send_follow_email_task(follower_username, followed_email):
    send_mail(
        subject='Você ganhou um novo seguidor!',
        message=f'{follower_username} começou a te seguir no Twitter Clone!',
        from_email='no-reply@twitterclone.com',
        recipient_list=[followed_email],
        fail_silently=True,
    )

class FollowView(generics.CreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        # Check if already following
        follower = request.user
        followed = serializer.validated_data['followed']
        
        # Verifica se o usuário já está seguindo o outro
        if Follow.objects.filter(follower=follower, followed=followed).exists():
            return Response({"detail": "Você já segue esse usuário."}, status=status.HTTP_400_BAD_REQUEST)

        # Cria o follow
        self.perform_create(serializer)
        
        # Envia o e-mail de notificação ao usuário seguido
        send_follow_email_task(follower.username, followed.email)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


# View para listar os seguidores de um usuário
class FollowersListView(generics.ListAPIView):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Follow.objects.filter(followed=user)


# View para listar os usuários que o usuário logado está seguindo
class FollowingListView(generics.ListAPIView):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Follow.objects.filter(follower=user)
