from datetime import datetime

from rest_framework import generics

from rest_framework.permissions import AllowAny

from users.models import User
from users.permissions import IsAdmin, IsOwnerYourself
from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """
    APTView for create User
    """

    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """
    APIView for read User
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdmin]


class UserUpdateAPIView(generics.UpdateAPIView):
    """
    APIView for update User
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsOwnerYourself]

    def perform_update(self, serializer):
        user = serializer.save(is_active=True)
        user.last_correct = datetime.now()
        user.save()


class UserDeleteAPIView(generics.DestroyAPIView):
    """
    APIView for delete User
    """

    queryset = User.objects.all()
    permission_classes = [IsAdmin]
