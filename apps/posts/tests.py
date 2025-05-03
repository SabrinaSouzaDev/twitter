from typing import cast
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.response import Response
from django.urls import reverse

from apps.accounts.models import User
from apps.posts.models import Post


class PostTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.post_create_url = reverse('post-list')  # ViewSet com basename='post'
        self.client.login(username='testuser', password='testpass')

    def test_create_post_success(self):
        """Usuário autenticado pode criar um post"""
        data = {'content': 'Hello world!'}
        response: Response = cast(Response, self.client.post(self.post_create_url, data))
        self.assertEqual(response.status_code, 201)

        post = Post.objects.first()
        self.assertIsNotNone(post, "Post não foi criado.")
        post = cast(Post, post)
        self.assertEqual(post.content, 'Hello world!')

    def test_create_post_empty_content(self):
        """Não deve permitir criar post com conteúdo vazio"""
        data = {'content': ''}
        response: Response = cast(Response, self.client.post(self.post_create_url, data))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Post.objects.count(), 0)

    def test_create_post_unauthenticated(self):
        """Usuário não autenticado não pode criar post"""
        self.client.logout()
        data = {'content': 'Unauthorized post'}
        response: Response = cast(Response, self.client.post(self.post_create_url, data))
        self.assertEqual(response.status_code, 403)
        self.assertEqual(Post.objects.count(), 0)

    def test_post_list(self):
        """Listar posts criados"""
        Post.objects.create(author=self.user, content='Post 1')
        Post.objects.create(author=self.user, content='Post 2')

        data = {'content': 'Unauthorized post'}
        response: Response = cast(Response, self.client.get(self.post_create_url, data))

        self.assertEqual(response.status_code, 200)

        response_data = response.json()
        self.assertEqual(len(response_data.get('results', [])), 2)
        
    def test_delete_post(self):
        """Usuário pode deletar o próprio post"""
        post = Post.objects.create(author=self.user, content='Post to delete')
        assert post.id is not None
        url = reverse('post-detail', args=[post.id])
        response: Response = cast(Response, self.client.delete(url))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Post.objects.count(), 0)

    def test_delete_post_other_user(self):
        """Usuário não pode deletar posts de outros"""
        other_user = User.objects.create_user(username='otheruser', password='otherpass')
        post = Post.objects.create(author=other_user, content='Other user post')   
        post = cast(Post, post)
        assert post.id is not None 
        url = reverse('post-detail', args=[post.id])
        response: Response = cast(Response, self.client.delete(url))
        self.assertEqual(response.status_code, 403)
        self.assertEqual(Post.objects.count(), 1)
