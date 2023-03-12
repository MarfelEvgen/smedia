from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.views.generic import CreateView

from blog.models import Post


class UserProfile(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='images/user')
    posts = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

