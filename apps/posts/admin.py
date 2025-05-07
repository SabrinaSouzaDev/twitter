# apps/posts/admin.py
from django.contrib import admin
from .models import Post, PostLike

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'content_snippet', 'created_at', 'updated_at')
    search_fields = ('author__username', 'content')
    list_filter = ('created_at',)

    def content_snippet(self, obj):
        return obj.content[:50]
    content_snippet.short_description = 'Conteúdo'

@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'created_at')
    search_fields = ('post__content', 'user__username')
    list_filter = ('created_at',)
