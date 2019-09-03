from django import forms
from .models import SingleTask, Company

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = SingleTask
        fields = ('text', 'done')

class EditTaskForm(forms.ModelForm):
    class Meta:
        model = SingleTask
        fields = ('text', 'done', 'user')
        exclude = ('user',)

class CompanyCreateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'owner_email', 'description')
