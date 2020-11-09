from rest_framework import serializers
from rest_framework.authtoken.models import Token

from app.models import RestRequest, RestResponse
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password', 'token',)

    @staticmethod
    def get_token(obj):
        token, created = Token.objects.get_or_create(user=obj)
        return token.key


class RestResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestResponse
        exclude = ('modified',)


class RequestSchedulerSerializer(serializers.ModelSerializer):
    response = RestResponseSerializer(read_only=True)

    class Meta:
        model = RestRequest
        fields = ('id', 'method', 'url', 'payload', 'started',
                  'completed', 'user', 'response',)
