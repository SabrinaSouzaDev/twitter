from rest_framework import serializers
from apps.accounts.serializers import PublicUserSerializer
from .models import Follow

class FollowSerializer(serializers.ModelSerializer):
    follower = PublicUserSerializer(read_only=True)
    followed = PublicUserSerializer(read_only=True)

    class Meta:
        model = Follow
        fields = ('id', 'follower', 'followed', 'created_at')
