from typing import Any, cast
from jsonschema import ValidationError
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from apps.follows.models import Follow
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from apps.accounts.models import User as CustomUser


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'bio',
            'followers_count',
            'following_count',
            'password'
        )
        extra_kwargs = {'password': {'write_only': True}}

    def validate_username(self, value):
        # Verifica se o nome de usuário foi alterado
        if self.instance and self.instance.username != value:
            if User.objects.filter(username=value).exists():
                raise ValidationError("Esse nome de usuário já está em uso.")
        
        return value


    def create(self, validated_data):
        password = validated_data.pop('password')
        validate_password(password)
        user = User.objects.create_user(password=password, **validated_data)
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            validate_password(password)
            instance.set_password(password)

        instance.save()
        return instance

    def get_followers_count(self, obj):
        # Corrigido para usar o related_name 'followers'
        return obj.followers.count()

    def get_following_count(self, obj):
        # Corrigido para usar o related_name 'following'
        return obj.following.count()

class PublicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'bio')
        read_only_fields = fields

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        user: CustomUser = cast(CustomUser, self.user)  # Explicitly cast self.user to CustomUser

        data.update({
            'username': user.username,
            'email': user.email,
        })

        return data
