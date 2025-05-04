# apps/posts/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache
from apps.posts.models import Post

@receiver(post_save, sender=Post)
def clear_feed_cache(sender, instance, **kwargs):
    cache_key = f"user_feed_{instance.author.pk}"
    cache.delete(cache_key)
