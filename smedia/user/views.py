from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, FormView

from blog.models import Post
from user.forms import RegisterUser, LoginUser
from user.models import UserProfile


@login_required
def profile(request):
    context = {
        'title': 'Profile',
        'post_user_list': Post.objects.filter(author=request.user).order_by('-date_create'),
    }
    return render(request, 'user/profile.html', context)


class SignUp(FormView):
    model = UserProfile
    form_class = RegisterUser
    template_name = 'registration/sign_up.html'
    success_url = reverse_lazy('newsfeed')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        avatar = form.cleaned_data['avatar']
        user = UserProfile.objects.create_user(username, password, avatar)
        login(self.request, user)

        form.save()
        return super().form_valid(form)


class UserLogin(LoginView):
    form_class = LoginUser
    template_name = 'user/login.html'

    context = {
        'title': 'login'
    }


class UserPofile(ListView):
    model = Post
    # template name html
    template_name = 'user/profile.html'
    # context_object_name = 'blog_post_user_list'

    def get_context_data(self, request,  **kwargs):
        queryset = Post.objects.filter(author=request.user)
        context = super().get_context_data(**kwargs)
        context['post_user_list'] = queryset.order_by('pk')
        return context