from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(username="testuser", password="testpass123")
        self.assertEqual(user.username, "testuser")
        self.assertTrue(user.check_password("testpass123"))

    def test_create_superuser(self):
        admin = User.objects.create_superuser(username="adminuser", password="adminpass123")
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)
