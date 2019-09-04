from django import forms
from .models import *

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
        fields = ('name', 'creator_email', 'description')


class CoGroupCreateForm(forms.ModelForm):
    class Meta:
        model = CompanyGroup
        fields = ('name', 'admin', 'member')
        exclude = ('admin', 'member')
