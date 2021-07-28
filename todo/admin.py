from django.contrib import admin
from .models import Task, Category

# Register your models here.
admin.site.register(Category)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    class Meta:
        # Give your model metadata by using an inner class Meta
        model = Task


