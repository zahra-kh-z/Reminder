from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .models import Task, Category
from django.utils import timezone
from django.urls import reverse_lazy


# Create your views here.
def home_page(request):
    return render(request, 'index.html')


class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'task_new.html'
    fields = '__all__'

    def form_valid(self, form):  # for add new task
        form.instance.task = self.request.user
        return super().form_valid(form)


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'


class TaskUpdateView(LoginRequiredMixin, UpdateView):  # new
    model = Task
    fields = '__all__'
    template_name = 'task_edit.html'


class TaskDeleteView(LoginRequiredMixin, DeleteView):  # new
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('task_list')


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = 'category_new.html'
    fields = '__all__'

    def form_valid(self, form):  # for add new task
        form.instance.category = self.request.user
        return super().form_valid(form)


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'


def cat_index(request):  # the index view
    # results = Task.objects.filter(category__isnull=False)
    # res = []
    # [res.append(result.category_id) for result in results]
    # # for result in results:
    # #     res.append(result.category_id)
    # categories2 = []
    # [categories2.append(x) for x in res if x not in categories2]

    # list_cat = []
    # list_cat_empty = []
    # for cat in categories:
    #     if Task.objects.filter(category__name=cat):
    #         list_cat.append(cat)
    #     else:
    #         list_cat_empty.append(cat)
    # category_full = list_cat
    # category_empty = list_cat_empty

    todos = Task.objects.get_all_tasks()  # quering all todos with the object manager
    categories = Category.objects.get_all_category() # getting all categories with object manager
    category_full = []
    category_empty = []
    for cat in categories:
        if Task.objects.filter(category__name=cat):
            category_full.append(cat)
        else:
            category_empty.append(cat)

    return render(request, "categories_list.html", {"todos": todos,
                                                    "category_empty": category_empty,
                                                    'category_full': category_full})


def show_expire(request):
    tasks_expire_list = Task.objects.task_expired()
    context = {"tasks_expire_list": tasks_expire_list}
    return render(request, 'task_expire.html', context)
