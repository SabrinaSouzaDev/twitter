from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from api.accounts.models import User
from api.posts.models import Post
from api.follows.models import Follow

class FeedTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='mainuser', password='mainpass')
        self.followed_user = User.objects.create_user(username='followed', password='followedpass')
        self.not_followed_user = User.objects.create_user(username='stranger', password='strangerpass')
        
        Follow.objects.create(follower=self.user, following=self.followed_user)

        Post.objects.create(author=self.followed_user, content='Followed user post')
        Post.objects.create(author=self.not_followed_user, content='Stranger post')

        self.feed_url = reverse('feed-list')  # Endpoint para listar feed
        self.client.login(username='mainuser', password='mainpass')

    def test_feed_shows_followed_posts(self):
        """Feed deve mostrar apenas posts dos usuários que sigo"""
        response = self.client.get(self.feed_url)
        self.assertEqual(response.status_code, 200)
        posts = [post['content'] for post in response.data['results']]
        self.assertIn('Followed user post', posts)
        self.assertNotIn('Stranger post', posts)

    def test_feed_empty_when_not_following(self):
        """Feed vazio se não seguir ninguém"""
        self.client.logout()
        new_user = User.objects.create_user(username='newuser', password='newpass')
        self.client.login(username='newuser', password='newpass')

        response = self.client.get(self.feed_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 0)

    def test_feed_requires_authentication(self):
        """Feed deve exigir autenticação"""
        self.client.logout()
        response = self.client.get(self.feed_url)
        self.assertEqual(response.status_code, 403)  # Forbidden
