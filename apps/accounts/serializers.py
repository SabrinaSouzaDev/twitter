
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'bio', 'profile_picture', 'followers_count')
        extra_kwargs = {'password': {'write_only': True}}  # A senha não deve ser retornada

    def get_followers_count(self, obj):
        return obj.followers.count()

    def create(self, validated_data):
        password = validated_data.pop('password', None)  # Retira a senha para processar separadamente
        user = User.objects.create(**validated_data)
        if password:
            user.set_password(password)  # Criptografa a senha
            user.save()
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['id'] = user.id
        token['email'] = user.email
        return token
