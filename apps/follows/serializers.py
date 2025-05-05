# apps/follows/serializers.py
from rest_framework import serializers
from apps.accounts.models import User
from apps.follows.models import Follow  # Usando o modelo CustomUser


class FollowSerializer(serializers.ModelSerializer):
    followed = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Follow
        fields = ['follower', 'followed']
        # Remova o UniqueTogetherValidator se for usar get_or_create
        validators = []

    def create(self, validated_data):
        follow, created = Follow.objects.get_or_create(
            follower=validated_data['follower'],
            followed=validated_data['followed']
        )
        return follow
