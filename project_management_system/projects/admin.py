from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description', 'language')
    prepopulated_fields = {'slug': ('name',)}
