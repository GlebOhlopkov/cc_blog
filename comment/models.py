from django.db import models

from post.models import Post
from users.models import User


class Comment(models.Model):
    """
    Model for Comment in blog
    """

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='author')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='post')
    text = models.TextField(verbose_name='text')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')
    last_correct = models.DateTimeField(null=True, blank=True, verbose_name='last_correct')

    def __str__(self):
        return f'{self.post} - {self.author}'

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
