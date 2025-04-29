from django.contrib import admin

from apps.follows.models import Follow


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('id', 'follower', 'followed', 'created_at')
    list_filter = ('created_at',)
    search_fields = (
        'follower__username', 
        'followed__username'
    )
    raw_id_fields = ('follower', 'followed')
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related(
            'follower', 'followed'
        )