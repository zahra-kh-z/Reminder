from django.utils import timezone
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


# Create your models here.
class TodoManager(models.Manager):
    """
    manager for Task and Category models.
    """
    use_in_migrations = True

    def get_all_tasks(self):
        """for return all object Task"""
        tasks = Task.objects.all()
        return tasks

    def task_expired(request):
        """for filter task that expire. if expire_date is less than not time return object task"""
        now = timezone.now()
        tasks_expire_list = Task.objects.filter(expire_date__lte=now)
        return tasks_expire_list

    def get_all_category(self):
        categories = Category.objects.all()
        return categories

    def my_category(self, cat):
        """for return all object Category"""
        categories = Category.objects.all(name=cat)
        return categories


class Category(models.Model):
    name = models.CharField(max_length=100)  # Like a varchar
    objects = TodoManager()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name  # name to be shown when called

    def get_absolute_url(self):
        """for url absolute"""
        return reverse('category_detail', args=[str(self.id)])


"""
If blank=True then the field model validation allows an empty value such as "" to be inputted by users. 
If blank=False then the validation will prevent empty values being inputted.
"""


class Task(models.Model):
    PRIORITY_TASK = [
        (0, 'بی اهمیت'),
        (1, 'کم اهمیت'),
        (2, 'توجه'),
        (3, 'قابل توجه'),
        (4, 'مهم'),
        (5, 'ضروری'),
    ]

    ENABLE = "enable"
    STATUS_TASK = [
        ('disable', 'غیرفعال'),
        (ENABLE, 'فعال'),
        ('doing', 'در حال انجام'),
        ('done', 'انجام شده'),
        ('expire', 'منقضی'),
        ('archive', 'ارشیو'),
    ]

    title = models.CharField(max_length=250)
    description = models.TextField()
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='ITEM')
    category = models.ForeignKey(Category, default="general", on_delete=models.CASCADE, related_name='ITEM')
    # category = models.ManyToManyField(Category, related_name='ITEM')
    priority = models.IntegerField(choices=PRIORITY_TASK, default=4)
    expire_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    objects = TodoManager()
    # slug = models.SlugField(null=False, unique=True)  # new
    # other fields
    # pip install pillow, PIL: Pillow Image Library
    picture = models.ImageField(default='TASK_4_Safe.png', upload_to='picture/')
    today = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_TASK, default=ENABLE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-expire_date"]  # ordering by the expire_date field

    def __str__(self):
        return self.title  # name to be shown when called

    def get_absolute_url(self):
        """for url absolute"""
        return reverse('task_detail', args=[str(self.id)])
        # return reverse('tasks:task_detail', kwargs={'slug': self.slug})  # new

    @property
    def timesince(self):
        """for return now time"""
        now = timezone.now()
        return now

    # def save(self, *args, **kwargs):  # new
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     return super().save(*args, **kwargs)
