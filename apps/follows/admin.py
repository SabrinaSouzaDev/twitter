# apps/follows/admin.py

from django.contrib import admin
from .models import Follow

# Modelo principal
@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('follower', 'followed', 'created_at')
    search_fields = ('follower__username', 'followed__username')
    list_filter = ('created_at',)
