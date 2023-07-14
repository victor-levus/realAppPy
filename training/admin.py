from django.contrib import admin

from . import models

# Register your models here.

    
@admin.register(models.Course )
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price']
    ordering = ['title']
    list_per_page = 15


@admin.register(models.Student )
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'created_at']
    ordering = ['first_name']
    list_per_page = 15