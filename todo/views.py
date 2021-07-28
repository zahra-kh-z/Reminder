from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render
from .models import Task, Category
from django.utils import timezone


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


def index(request):  # the index view
    todos = Task.objects.all()  # quering all todos with the object manager
    categories = Category.objects.all()  # getting all categories with object manager
    results = Task.objects.filter(category__isnull=False)
    res = []
    for a in results:
        res.append(a.category_id)
    categories2 = []
    [categories2.append(x) for x in res if x not in categories2]

    list_cat = []
    list_cat_empty = []
    for c in categories:
        if Task.objects.filter(category__name=c):
            list_cat.append(c)
        else:
            list_cat_empty.append(c)
    category_full = list_cat
    category_empty = list_cat_empty

    return render(request, "categories_list.html", {'categories2': categories2,
                                                    "categories": categories,
                                                    "todos": todos,
                                                    "category_empty": category_empty,
                                                    'category_full': category_full})


def show_expire(request):
    now = timezone.now()
    tasks_expire_list = Task.objects.filter(expire_date__lt=now)
    return render(request, 'task_expire.html', {"tasks_expire_list": tasks_expire_list})
