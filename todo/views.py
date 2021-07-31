from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404

from .forms import TaskForm
from .models import Task, Category
from django.urls import reverse_lazy


# Create your views here.
def home_page(request):
    return render(request, 'index.html')


class TaskListView(ListView):
    """classView for show task list"""
    model = Task
    template_name = 'task_list.html'


class TaskCreateView(LoginRequiredMixin, CreateView):
    """classView for create task"""
    model = Task
    template_name = 'task_new.html'
    # fields = '__all__'  # if not use forms.py
    """for use forms.py for new task"""
    form_class = TaskForm
    # success_url = reverse_lazy('task_new')  # for stay in task_new form after add task

    def form_valid(self, form):  # for add new task
        form.instance.task = self.request.user
        return super().form_valid(form)


class TaskDetailView(DetailView):
    """classView for show detail task"""
    model = Task
    template_name = 'task_detail.html'


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    """classView for editing task if is admin login"""
    model = Task
    fields = '__all__'
    template_name = 'task_edit.html'


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    """classView for deleting task if is admin login"""
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('task_list')


class CategoryCreateView(LoginRequiredMixin, CreateView):
    """classView for create category if is admin login"""
    model = Category
    template_name = 'category_new.html'
    fields = '__all__'

    def form_valid(self, form):  # for add new task
        form.instance.category = self.request.user
        return super().form_valid(form)


class CategoryDetailView(DetailView):
    """classView for show category detail after create"""
    model = Category
    template_name = 'category_detail.html'


def cat_index(request):
    """for return query content of task if category name is equal with category classification"""
    todos = Task.objects.get_all_tasks()  # quering all todos with the object manager
    categories = Category.objects.get_all_category()  # getting all categories with object manager
    category_full = []  # category list with task
    category_empty = []  # category list without task
    for cat in categories:
        if Task.objects.filter(category__name=cat):
            category_full.append(cat)
        else:
            category_empty.append(cat)

    return render(request, "categories_list.html", {"todos": todos,
                                                    "category_empty": category_empty,
                                                    'category_full': category_full})


def show_expire(request):
    """for show expire task with query manager"""
    tasks_expire_list = Task.objects.task_expired()
    context = {"tasks_expire_list": tasks_expire_list}
    return render(request, 'task_expire.html', context)


class TaskDataTable(ListView):
    """class view for show task with datatable"""
    model = Task
    template_name = 'datatable.html'

# def workWithApi(request):
#     """for test work ajax and api on template"""
#     return render(request,'t.html',{})
