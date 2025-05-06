from rest_framework import serializers
from apps.accounts.serializers import PublicUserSerializer
from apps.posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    author = PublicUserSerializer(read_only=True)
    like_count = serializers.IntegerField(read_only=True)
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id', 'author', 'content', 'image',
            'created_at', 'updated_at', 'like_count', 'is_liked'
        ]
        read_only_fields = ('author', 'created_at', 'updated_at', 'like_count', 'is_liked')

    def get_is_liked(self, obj):
        request = self.context.get('request', None)
        user = getattr(request, 'user', None)
        if user and user.is_authenticated:
            return obj.likes.filter(user=user).exists()
        return False

    def create(self, validated_data):
        # Adiciona o autor automaticamente ao validated_data
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)
