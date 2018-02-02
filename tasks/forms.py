from django import forms
from .models import Task


class DateInput(forms.DateInput):
    input_type = 'date'


class TaskForm(forms.ModelForm):
    """
    A model form for a Task object.
    """
    class Meta:
        exclude = ['pk', 'owner', 'complete_time']
        model = Task
        widgets = {
            'due_date': DateInput()
        }
