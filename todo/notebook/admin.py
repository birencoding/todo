from django.contrib import admin

# Register your models here.
from .models import Notebook


@admin.register(Notebook)
class NotebookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('author', 'created_at', 'updated_at')
    ordering = ('-updated_at',)
    date_hierarchy = 'created_at'