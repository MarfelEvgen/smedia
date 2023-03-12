from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import Post
from user.forms import AddPost


class AllUserPostListView(ListView):
    # model Post in models.py
    model = Post
    # template name html
    template_name = 'blog/newsfeed.html'
    # context_object_name = 'blog_post_user_list'


    def get_context_data(self, **kwargs):
        # user = get_object_or_404(User, username=self.kwargs.get('username'))
        queryset = Post.objects.all()
        context = super().get_context_data(**kwargs)
        context['blog_post_user_list'] = queryset.order_by('-date_create')
        return context


# class PostCreateView(LoginRequiredMixin, CreateView):
#     model = Post
#     fields = ['title', 'content', 'post_foto']
#     template_name = 'blog/create_post.html'
#     success_url = reverse_lazy('profile')
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

def addpage(request):
    if request.method == 'POST':
        form = AddPost(data=request.POST)
        if form.is_valid():
            print('sdfsdf')

    else:
        form = AddPost()
        print('1111')

    context = {
        'form': form,
        'title': 'add post'
    }

    return render(request, 'blog/create_post.html', context)