from django.urls import path
from .views import *
from .apiviews import TaskList, TaskDetail
urlpatterns = [
    path('', home_page, name='home'),
    path('task/', TaskListView.as_view(), name='task_list'),
    path('new/', TaskCreateView.as_view(), name='task_new'), # new
    path('task_detail/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    # path('<slug:slug>/', TaskDetailView.as_view(), name='task_detail'),
    path('<int:pk>/edit/', TaskUpdateView.as_view(), name='task_edit'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('new_cat/', CategoryCreateView.as_view(), name='category_new'), # new
    path('cat_detail/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('category/', cat_index, name='categories_list'),
    path('task_expire/', show_expire, name='show_expire'),
    path("tasks_json/", TaskList.as_view(), name="tasks_json_list"),
    path("tasks_json/<int:pk>/", TaskDetail.as_view(), name="tasks_json_detail"),
]
