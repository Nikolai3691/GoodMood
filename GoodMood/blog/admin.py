from django.contrib import admin
from .models import *


class PublicationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'photo', 'is_published', 'time_create')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'time_create')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'is_published', 'time_create', 'person_comment')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'person_comment')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}


class RecordsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'record_closed', 'record_open', 'person_record', 'service')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'record_closed', 'record_open', 'service')
    list_filter = ('record_closed', 'record_open')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Publications, PublicationsAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Records, RecordsAdmin)
