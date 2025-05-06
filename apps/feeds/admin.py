# tweets/admin.py

from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from apps.posts.models import Post


@admin.register(Post)
class TweetAdmin(SimpleHistoryAdmin):
    pass
