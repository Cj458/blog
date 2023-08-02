from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.db.models.aggregates import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse

from .models import Post, User


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ['user', 'title']
    list_per_page = 10
    list_filter = ['user']
    search_fields = ['title__istartswith', 'user__istartswith']


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ('name',"username", 'email',  "password1", "password2"),
            },
        ),
    )
    list_display=['name', 'email', 'posts_count']
    list_filter = ['name']
    search_fields = ['name__istartswith']

    @admin.display(ordering='posts_count')
    def posts_count(self, user):
        url = (
            reverse('admin:base_post_changelist')
            + '?'
            + urlencode({
                'user__id': str(user.id)
            }))
        return format_html('<a href="{}">{} Posts</a>', url, user.posts_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            posts_count=Count('posts')
        )

