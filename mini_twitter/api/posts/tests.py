from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from api.accounts.models import User
from api.posts.models import Post

class PostTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.post_create_url = reverse('post-list')  # Você pode ter usado um ViewSet para posts
        self.client.login(username='testuser', password='testpass')

    def test_create_post_success(self):
        """Usuário autenticado pode criar um post"""
        data = {'content': 'Hello world!'}
        response = self.client.post(self.post_create_url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.first().content, 'Hello world!')

    def test_create_post_empty_content(self):
        """Não deve permitir criar post com conteúdo vazio"""
        data = {'content': ''}
        response = self.client.post(self.post_create_url, data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Post.objects.count(), 0)

    def test_create_post_unauthenticated(self):
        """Usuário não autenticado não pode criar post"""
        self.client.logout()
        data = {'content': 'Unauthorized post'}
        response = self.client.post(self.post_create_url, data)
        self.assertEqual(response.status_code, 403)  # Permission Denied

    def test_post_list(self):
        """Listar posts criados"""
        Post.objects.create(author=self.user, content='Post 1')
        Post.objects.create(author=self.user, content='Post 2')

        response = self.client.get(self.post_create_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 2)

    def test_delete_post(self):
        """Usuário pode deletar o próprio post"""
        post = Post.objects.create(author=self.user, content='Post to delete')
        url = reverse('post-detail', args=[post.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Post.objects.count(), 0)

    def test_delete_post_other_user(self):
        """Usuário não pode deletar posts de outros"""
        other_user = User.objects.create_user(username='otheruser', password='otherpass')
        post = Post.objects.create(author=other_user, content='Other user post')

        url = reverse('post-detail', args=[post.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(Post.objects.count(), 1)
