from rest_framework import serializers
from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    fullName = serializers.CharField(source='full_name')

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'fullName', 'joined']
