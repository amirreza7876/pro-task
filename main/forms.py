from django import forms
from .models import SingleTask, GroupTask

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = SingleTask
        fields = ('text', 'done')

class EditTaskForm(forms.ModelForm):
    class Meta:
        model = SingleTask
        fields = ('text', 'done', 'user')
        exclude = ('user',)

# TODO:
class GroupJoinForm(forms.Form):
    pivate_key = forms.CharField(max_length=128)
