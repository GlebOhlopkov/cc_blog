from rest_framework import serializers

from comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for Comment Model
    """

    class Meta:
        model = Comment
        fields = '__all__'
