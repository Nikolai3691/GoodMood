from django.contrib import admin
from .models import *


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'photo', 'is_published', 'worker')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'write_up', 'worker')
    list_editable = ('is_published',)
    list_filter = ('is_published',)
    prepopulated_fields = {'slug': ('title',)}


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Services, ServicesAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
