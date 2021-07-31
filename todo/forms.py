from django import forms
from django.forms import ModelForm, DateTimeField
from .MinimalSplitDateTimeMultiWidget import *
from django.contrib.admin import widgets

from .models import Task


class DateInput(forms.DateInput):
    input_type = 'date'


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'expire_date': DateInput(),
        }
        """
        for use with DateTime in separate fields, date and time.
        if use this should comment above widgets.
        """
        # widgets = {
        #     'expire_date': widgets.AdminSplitDateTime,
        # }
        # expire_date = DateTimeField(widget=MinimalSplitDateTimeMultiWidget())
