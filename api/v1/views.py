from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import filters, permissions, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (CreateModelMixin, ListModelMixin,
                                   RetrieveModelMixin, UpdateModelMixin,
                                   DestroyModelMixin)

from app.models import RestRequest
from .serializers import UserSerializer, RequestSchedulerSerializer

from django.contrib.auth import get_user_model

User = get_user_model()


class UserSignupView(CreateModelMixin, GenericViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(dict(token=token.key))


class RequestSchedulerView(GenericViewSet, CreateModelMixin, ListModelMixin,
                           RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = RestRequest.objects.all()
    permission_classes = [permissions.AllowAny]  # it maybe token based auth if needed.
    serializer_class = RequestSchedulerSerializer
