from django.db import models
from django.contrib.auth.models import AbstractUser


class Note(models.Model):
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created_at')

    def __str__(self):
        return f'{self.content}'

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
        ordering = ['created_at']


class User(AbstractUser):
    email = models.EmailField(verbose_name='Email', unique=True)
