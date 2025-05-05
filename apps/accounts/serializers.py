from rest_framework import serializers
from django.contrib.auth import get_user_model
from apps.follows.models import Follow 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

# Serializer usado para criar usuários (registro)
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'bio', 'followers_count', 'following_count', 'password')

    def get_followers_count(self, obj):
        return Follow.objects.filter(followed=obj).count()

    def get_following_count(self, obj):
        return Follow.objects.filter(follower=obj).count()

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

# exibição pública posts
class PublicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'bio')
        read_only_fields = fields

# JWT para incluir campos adicionais no token
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['id'] = user.id
        token['email'] = user.email
        return token
