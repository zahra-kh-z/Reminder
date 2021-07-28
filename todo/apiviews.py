from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Task
from .serializers import TaskSerializer


class TaskList(APIView):
    def get(self, request):
        tasks = Task.objects.all()[:20]
        data = TaskSerializer(tasks, many=True).data
        return Response(data)


class TaskDetail(APIView):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        data = TaskSerializer(task).data
        return Response(data)
