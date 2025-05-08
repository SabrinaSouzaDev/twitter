from django.contrib import admin
from .models import Feed, FeedImage


@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at']
    search_fields = ['user__username']
    list_filter = ['created_at']
    ordering = ['-created_at']

@admin.register(FeedImage)
class FeedImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'feed', 'created_at']
    list_filter = ['created_at']
    ordering = ['-created_at']
    search_fields = ['feed__user__username']
    raw_id_fields = ['feed']