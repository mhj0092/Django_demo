from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'completed', 'due_date']
    list_filter = ['completed', 'user']
    search_fields = ['title']