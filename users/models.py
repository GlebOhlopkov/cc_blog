from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(unique=True, max_length=100, verbose_name='username')
    email = models.EmailField(verbose_name='email')
    phone = models.CharField(max_length=50, verbose_name='phone')
    birthday = models.DateField(verbose_name='birthday')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')
    last_correct = models.DateTimeField(null=True, blank=True, verbose_name='last_correct')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
