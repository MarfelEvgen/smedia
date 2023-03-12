from django.contrib import admin
from blog.models import Post

@admin.register(Post)
class PageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date_create']
    list_display_links = ['id', 'title',]
    prepopulated_fields = {'slug': ('title',)}
