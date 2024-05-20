from datetime import datetime

from rest_framework import generics

from rest_framework.permissions import AllowAny, IsAdminUser

from comment.models import Comment
from comment.permissions import IsOwner
from comment.serializers import CommentSerializer


class CommentCreateAPIView(generics.CreateAPIView):
    """
    APTView for create Comment
    """

    serializer_class = CommentSerializer


class CommentRetrieveAPIView(generics.RetrieveAPIView):
    """
    APIView for read Comment
    """

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [AllowAny]


class CommentUpdateAPIView(generics.UpdateAPIView):
    """
    APIView for update Comment
    """

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAdminUser, IsOwner]

    def perform_update(self, serializer):
        comment = serializer.save()
        comment.last_correct = datetime.now()
        comment.save()


class CommentDeleteAPIView(generics.DestroyAPIView):
    """
    APIView for delete Comment
    """

    queryset = Comment.objects.all()
    permission_classes = [IsAdminUser, IsOwner]
