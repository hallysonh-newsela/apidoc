from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .serializers import UserSerializer

User = get_user_model()


def login(self):
    self.superuser = User.objects.create_superuser(
        'test', 'test@test.com', 'testpass')
    self.client.login(username='test', password='testpass')


class CreateUserTest(APITestCase):
    def setUp(self):
        login(self)
        self.data = {'username': 'mike', 'fullName': 'Mike Tyson'}

    def test_can_create_user(self):
        response = self.client.post(reverse('user-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadUserTest(APITestCase):
    def setUp(self):
        login(self)
        self.user = User.objects.create(username="mike")

    def test_can_read_user_list(self):
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_user_detail(self):
        response = self.client.get(reverse('user-detail', args=[self.user.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateUserTest(APITestCase):
    def setUp(self):
        login(self)
        self.user = User.objects.create(username="mike", first_name="Tyson")
        self.data = UserSerializer(self.user).data
        self.data.update({'first_name': 'Changed'})

    def test_can_update_user(self):
        response = self.client.put(
            reverse('user-detail', args=[self.user.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
