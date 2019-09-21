from django import forms
from .models import *

# class CreateTaskForm(forms.ModelForm):
#     class Meta:
#         model = SingleTask
#         fields = ('text', 'done')
#         labels = {'name': ''}
#         widget = {'name': forms.TextInput(attrs={'placeholder': 'Text'})}
#
#
# class EditTaskForm(forms.ModelForm):
#     class Meta:
#         model = SingleTask
#         fields = ('text', 'done', 'user')
#         exclude = ('user',)

class CompanyCreateForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('name', 'creator_email', 'description')
        labels = {
            'name': '',
            'creator_email': '',
            'description': ''
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Team Name'}),
            'creator_email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'description': forms.TextInput(attrs={'placeholder': 'Description'})
        }




class MemberJoinForm(forms.Form):
    secret_key = forms.CharField(max_length=128, widget=forms.PasswordInput)


# class CoGroupCreateForm(forms.ModelForm):
#     class Meta:
#         model = CompanyGroup
#         fields = ('name', 'admin', 'member')
#         exclude = ('admin', 'member')

class SearchUserForm(forms.Form):
    usern = forms.CharField(max_length=1024, label='',widget=forms.TextInput(attrs={'placeholder': 'Usernames'}),
                            error_messages={'required': 'Please let us\
                                            know what to call you!'})


class GroupTaskCreateForm(forms.ModelForm):
    class Meta:
        model = TeamTask
        fields = ('text', 'done')


class SearchForTeam(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('search_id',)
        widgets = {
            'search_id': forms.TextInput(attrs={'placeholder': 'Your Team ID'})
        }
        labels = {
            'search_id': ''
        }
