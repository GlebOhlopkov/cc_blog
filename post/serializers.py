from rest_framework import serializers

from comment.serializers import CommentSerializer
from post.models import Post
from post.validators import OverAgeValidator, WrongTittleValidator


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for Post Model
    """

    comments = CommentSerializer(source='comment_set.all', many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        validators = [OverAgeValidator(), WrongTittleValidator(), ]
