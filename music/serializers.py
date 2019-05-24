from rest_framework import serializers
from django.contrib.auth.models import User

from music.models import Songs


class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ("title", "artist")


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", 'password')


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", 'password')
