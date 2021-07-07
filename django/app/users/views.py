from django.conf import settings
from django.http.response import HttpResponse
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


def index(_):
    env = settings.DEBUG and 'dev' or 'prod'
    return HttpResponse(f'Hello from Django App! (ENV: {env})', status=status.HTTP_200_OK)


user_list = UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
})
