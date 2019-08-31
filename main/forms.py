from django import forms
from .models import SingleTask

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = SingleTask
        fields = ('text', 'done')

class EditTaskForm(forms.ModelForm):
    class Meta:
        model = SingleTask
        fields = ('text', 'done', 'user')
        exclude = ('user',)
