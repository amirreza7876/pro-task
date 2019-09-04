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


class EmployeeJoinForm(forms.Form):
    secret_key = forms.CharField(max_length=128, widget=forms.PasswordInput)


class CoGroupCreateForm(forms.ModelForm):
    class Meta:
        model = CompanyGroup
        fields = ('name', 'admin', 'member')
        exclude = ('admin', 'member')

class SearchUserForm(forms.Form):
    usern = forms.CharField(max_length=1024, label='usernames',error_messages={'required': 'Please let us know what to call you!'})


class GroupTaskCreateForm(forms.ModelForm):
    class Meta:
        model = GroupTask
        fields = ('text', 'done')
