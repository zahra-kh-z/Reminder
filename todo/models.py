from django.utils import timezone
from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)  # Like a varchar

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name  # name to be shown when called


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
    category = models.ForeignKey(Category, default="general", on_delete=models.CASCADE)
    priority = models.IntegerField(choices=PRIORITY_TASK, default=4)
    expire_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    # other fields
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

    @property
    def timesince(self):
        """for return now time"""
        now = timezone.now()
        return now
