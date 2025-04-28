from rest_framework import generics
from .models import Follow
from .serializers import FollowSerializer

class FollowCreateView(generics.CreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
