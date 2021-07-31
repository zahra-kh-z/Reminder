from rest_framework import serializers
from .models import Task


# https://howtojsonapi.com/django.html
class TaskSerializer(serializers.ModelSerializer):
    """convert data app to json"""

    class Meta:
        model = Task
        fields = '__all__'
