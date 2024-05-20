from datetime import datetime

from rest_framework import generics

from rest_framework.permissions import AllowAny, IsAdminUser

from post.models import Post
from post.permissions import IsOwner
from post.serializers import PostSerializer


class PostCreateAPIView(generics.CreateAPIView):
    """
    APTView for create Post
    """

    serializer_class = PostSerializer


class PostRetrieveAPIView(generics.RetrieveAPIView):
    """
    APIView for read Post
    """

    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [AllowAny]


class PostUpdateAPIView(generics.UpdateAPIView):
    """
    APIView for update Post
    """

    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAdminUser, IsOwner]

    def perform_update(self, serializer):
        post = serializer.save()
        post.last_correct = datetime.now()
        post.save()


class PostDeleteAPIView(generics.DestroyAPIView):
    """
    APIView for delete Post
    """

    queryset = Post.objects.all()
    permission_classes = [IsAdminUser, IsOwner]
