from django.contrib import admin
from apps.feeds.models import Feed

@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at')