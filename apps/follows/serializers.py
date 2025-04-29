from rest_framework import serializers

from apps.accounts.serializers import UserSerializer
from apps.follows.models import Follow



class FollowSerializer(serializers.ModelSerializer):
    follower = UserSerializer(read_only=True)
    followed = UserSerializer(read_only=True)

    class Meta:
        model = Follow
        fields = '__all__'