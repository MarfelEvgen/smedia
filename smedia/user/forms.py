from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import Form
from django.shortcuts import redirect
from django.views.generic import CreateView

from blog.models import *
from user.models import UserProfile


class AddPost(forms.Form):
    title = forms.CharField(max_length=255)
    content = forms.CharField(max_length=1000)
    post_foto = forms.ImageField()

    class Meta:
        model = Post
        field = ('title', 'content', 'post_foto')


class RegisterUser(UserCreationForm):
    model = UserProfile
    form_class = UserCreationForm
    template_name = 'user/sign_up.html'
    success_url = 'user/profile.html'

    class Meta:
        field = ('name', 'password', 'avatar')


class LoginUser(AuthenticationForm):
    pass
