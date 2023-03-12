from django.contrib import admin

from user.models import UserProfile


@admin.register(UserProfile)
class PageUser(admin.ModelAdmin):
    list_display = ['name', 'avatar']
    list_display_links = ['name']

