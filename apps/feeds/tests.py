from rest_framework.response import Response
from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse

from apps.accounts.models import User
from apps.follows.models import Follow
from apps.posts.models import Post


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
        response = self.client.get(self.feed_url)  # Tipo padrão HttpResponse
        response = Response(response)  # Fazendo o cast para Response

        self.assertEqual(response.status_code, 200)

        # Agora verificamos se a resposta tem o formato esperado
        if isinstance(response.data, dict):
            posts = [post['content'] for post in response.data.get('results', [])]
            self.assertIn('Followed user post', posts)
            self.assertNotIn('Stranger post', posts)
        else:
            self.fail(f"Expected response.data to be a dict, but got {type(response.data)}")

    def test_feed_empty_when_not_following(self):
        """Feed vazio se não seguir ninguém"""
        self.client.logout()
        new_user = User.objects.create_user(username='newuser', password='newpass')
        self.client.login(username='newuser', password='newpass')

        response = self.client.get(self.feed_url)  # Tipo padrão HttpResponse
        response = Response(response)  # Fazendo o cast para Response
        self.assertEqual(response.status_code, 200)

        if isinstance(response.data, dict):
            self.assertEqual(len(response.data.get('results', [])), 0)
        else:
            self.fail(f"Expected response.data to be a dict, but got {type(response.data)}")

    def test_feed_requires_authentication(self):
        """Feed deve exigir autenticação"""
        self.client.logout()
        response = self.client.get(self.feed_url)  # Tipo padrão HttpResponse
        response = Response(response)  # Fazendo o cast para Response
        self.assertEqual(response.status_code, 403)  # Forbidden
