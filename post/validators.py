from rest_framework import serializers

from post.services import check_tittle, check_age
from users.models import User


class OverAgeValidator:
    """
    Validator to check age of author
    """

    def __call__(self, value):
        author_post = value.get('author')
        if author_post:
            author = User.objects.get(pk=author_post.id)
            if check_age(author.birthday):
                raise serializers.ValidationError(
                    'You cant public this post. Your age must be over 18 y.o.')


class WrongTittleValidator:
    """
    Validator to check banned words in title
    """

    def __call__(self, value):
        title = value.get('title')
        if check_tittle(title):
            raise serializers.ValidationError(
                'You used banned word in tittle. Please enter different title')
