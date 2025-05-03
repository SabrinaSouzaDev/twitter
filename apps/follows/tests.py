from django.test import TestCase
from django.contrib.auth import get_user_model

from apps.follows.models import Follow




User = get_user_model()


class FollowModelTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="user1", password="password123")
        self.user2 = User.objects.create_user(username="user2", password="password123")

    def test_follow_another_user(self):
        follow = Follow.objects.create(follower=self.user1, following=self.user2)
        self.assertEqual(Follow.objects.count(), 1)
        self.assertEqual(follow.follower, self.user1)
        self.assertEqual(follow.followed, self.user2)

    def test_cannot_follow_self(self):
        with self.assertRaises(Exception):
            Follow.objects.create(follower=self.user1, following=self.user1)

    def test_unique_follow_constraint(self):
        Follow.objects.create(follower=self.user1, following=self.user2)
        with self.assertRaises(Exception):
            Follow.objects.create(follower=self.user1, following=self.user2)
