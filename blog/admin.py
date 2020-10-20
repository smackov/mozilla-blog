from django.contrib import admin
from .models import Blog, Blogger, BlogComment


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'blogger', 'post_date')
    list_filter = ('blogger', 'post_date')


@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'date_of_death')
    fields = ['user', ('date_of_birth', 'date_of_death')]


