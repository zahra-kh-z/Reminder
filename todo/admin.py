from django.contrib import admin
from .models import Task, Category

# Register your models here.
# admin.site.register(Category)

"""
for show apps and fields in admin panel you should registered your models.
"""


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    class Meta:
        # Give your model metadata by using an inner class Meta
        model = Task


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category
