from django.contrib import admin

from .models import Group, Post


class GroupAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
    )
    search_fields = (
        'slug',
    )
    empty_value_display = '-пусто-'


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
    )
    search_fields = (
        'text',
    )
    list_filter = (
        'pub_date',
        'group',
    )
    list_editable = (
        'group',
    )
    empty_value_display = '-пусто-'


admin.site.register(Group, GroupAdmin)
admin.site.register(Post, PostAdmin)
