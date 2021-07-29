from rest_framework import serializers
from .models import Task

# https://howtojsonapi.com/django.html
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
