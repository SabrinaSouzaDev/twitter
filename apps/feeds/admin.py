# tweets/admin.py

from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from apps.feeds.models import Feed



@admin.register(Feed)
class TweetAdmin(SimpleHistoryAdmin):
    pass
