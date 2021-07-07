from django.test import TestCase

from .models import User


class UserTest(TestCase):
    """ Test module for User model """

    def setUp(self):
        User.objects.create(
            username="teste1",
            first_name="First1",
            last_name="Last")
        User.objects.create(
            username="teste2",
            first_name="First2",
            last_name="Last")

    def test_user(self):
        user01 = User.objects.get(username="teste1")
        user02 = User.objects.get(username="teste2")
        self.assertEqual(user01.full_name, "First1 Last")
        self.assertEqual(user02.full_name, "First2 Last")
