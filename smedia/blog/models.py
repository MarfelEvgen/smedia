from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.utils.text import slugify


class Post(models.Model):

    class Meta:
        verbose_name = 'Create Post'
        verbose_name_plural = 'Create Posts'

    title = models.CharField(max_length=50, db_index=True)
    content = models.TextField(max_length=1000, blank=True, null=True, help_text='Enter something')
    content = RichTextField(help_text="max 1000 characters", max_length=1000)#redactor ckeditor
    post_foto = models.ImageField(upload_to='images/post_foto')
    date_create = models.DateTimeField(default=timezone.now)
    date_update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=50)

    #like and saved posts
    likes_post = models.ManyToManyField(User, related_name='post_likes', blank=True)
    saved_posts = models.ManyToManyField(User, related_name="blog_posts_save", blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def total_likes(self):
        return self.likes_post.count()

    def total_saved_posts(self):
        return self.saved_posts.count()

    def get_absolute_url(self):
        return reverse('profile')

    def __str__(self):
        return self.title
