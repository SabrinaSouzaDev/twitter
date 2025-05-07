from django.contrib import admin
from .models import Post, PostLike

class PostLikeInline(admin.TabularInline):
    model = PostLike
    extra = 0

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'content_short', 'created_at', 'like_count')
    list_filter = ('created_at', 'author')
    search_fields = ('content', 'author__username')
    inlines = [PostLikeInline]
    
    def content_short(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    content_short.short_description = 'Content'
    
    def like_count(self, obj):
        return obj.likes.count()
    like_count.short_description = 'Likes'

@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'post__content')