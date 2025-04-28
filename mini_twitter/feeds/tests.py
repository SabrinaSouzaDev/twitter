from django.test import TestCase
from django.contrib.auth import get_user_model
from posts.models import Post
from follows.models import Follow

User = get_user_model()

class FeedTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="user1", password="password123")
        self.user2 = User.objects.create_user(username="user2", password="password123")

        self.post_by_user2 = Post.objects.create(author=self.user2, content="Hello World!")
        Follow.objects.create(follower=self.user1, following=self.user2)

    def test_feed_content(self):
        # Simula o "feed" sem fazer requisição HTTP
        posts = Post.objects.filter(author__followers_following__follower=self.user1)
        self.assertIn(self.post_by_user2, posts)
