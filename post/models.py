from django.db import models

from users.models import User


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='title')
    text = models.TextField(verbose_name='text')
    image = models.ImageField(upload_to='post/', null=True, blank=True, verbose_name='image')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='author')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')
    last_correct = models.DateTimeField(null=True, blank=True, verbose_name='last_correct')

    def __str__(self):
        return f'{self.title} ({self.author})'

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
