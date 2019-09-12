from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required, permission_required
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import re

class IndexView(TemplateView):
    template_name = 'main/index.html'


@login_required
def create_task(request):
    if request.method == 'POST':
        user = request.user
        create_form = CreateTaskForm(request.POST)
        if create_form.is_valid():
            new_post = SingleTask(user=user,
                                  text=create_form.cleaned_data['text'],
                                  done=create_form.cleaned_data['done'])
            new_post.save()
            return redirect('account:profile_detail',username=user.username)
    else:
        create_form = CreateTaskForm()
    return render(request, 'main/create_task.html', {'form': create_form})


@login_required
# @permission_required ??
def edit_task(request, id):
    task = get_object_or_404(SingleTask,id=id, user=request.user)
    user = request.user
    if request.method == 'POST':
        edit_form = EditTaskForm(request.POST)
        if edit_form.is_valid():
            task.text = edit_form.cleaned_data['text']
            task.done = edit_form.cleaned_data['done']
            task.save()
            return redirect('account:profile_detail',username=user.username)
    else:
        edit_form = EditTaskForm()
    return render(request, 'main/edit_task.html', {'task': task,
                                                   'form': edit_form})


def company_register(request):
    if request.method == 'POST':
        company_form = CompanyCreateForm(request.POST)
        if company_form.is_valid():
            new_company = company_form.save(commit=False)
            new_company.creator = request.user
            new_company.save()
            return render(request, 'main/company_registered.html', {'new_company': new_company})
    else:
        company_form = CompanyCreateForm()

    return render(request, 'main/company_registration.html', {'form':company_form})



def company_detail(request, id):
    company = get_object_or_404(Company, id=id)
    if request.user in company.employee.all():
            return render(request, 'main/company_detail.html', {'company': company})
    elif request.user in company.owner.all():
            return render(request, 'main/company_detail.html', {'company': company})
    elif request.user not in company.employee.all():
        if request.user not in company.owner.all():
            if request.method == 'POST':
                join_form = EmployeeJoinForm(request.POST)
                if join_form.is_valid():
                    form = join_form.cleaned_data
                    if form['secret_key'] == company.secret_key:
                        company.employee.add(request.user)
                        return redirect('main:company_detail', id=company.id)
                    else:
                        return redirect('account:dashboard')
            else:
                join_form = EmployeeJoinForm()
        return render(request, 'main/join_to_co.html', {'form': join_form})

    return HttpResponse('error')


@login_required
def group_create(request):
    if request.user.co_own.all():
        if request.method == 'POST':
            form = CoGroupCreateForm(request.POST)
            if form.is_valid:
                new_group = form.save(commit=False)
                new_group.admin = request.user
                new_group.save()
                group = Group.objects.get(id=new_group.id)
                group.member.add(request.user)
                return render(request, 'main/group_created.html', {'group': new_group})
        else:
            form = CoGroupCreateForm()
    else:
        return redirect('main:company_register')
    return render(request, 'main/register_group.html', {'form': form})


@login_required
def group_detail(request, id):
    group = get_object_or_404(Group, id=id)
    tasks = group.tasks.all()
    return render(request, 'main/group_detail.html', {'group': group, 'tasks': tasks})


@login_required
def user_groups(request):
    user = request.user
    groups = user.groups_in.all()

    return render(request, 'main/user_groups_in.html', {'user': user,
                                                        'groups': groups})


def user_companies(request):
    user = request.user
    companies_in = user.workat.all()
    return render(request, 'main/user_companies_in.html', {'user': user,
                                                        'companies': companies_in})

@login_required
def add_member(request, id):
    group = get_object_or_404(Group, id=id)
    if request.user in group.member.all() or request.user == group.admin:
        if request.method == 'POST':
            form = SearchUserForm(request.POST)
            if form.is_valid():
                list_name = form.cleaned_data['usern']
                usernames = re.sub('[^\w]', ' ', list_name).split()
                user_not_found = []
                user_exists = []
                for username in usernames:
                    try:
                        user = User.objects.get(username=username)
                        group.member.add(user)
                        if user in group.member.all():
                            user_exists.append(username)
                        group.save()
                    except ObjectDoesNotExist as not_found:
                        user_not_found.append(username)
                return render(request, 'main/search_user_forgp.html',
                              {'form': form,
                              'group': group,
                              'user_not_found': user_not_found,
                              'success_users': username,
                              'user_exists': user_exists})
                # group.save()
                return redirect('main:group_detail', id=group.id)
        else:
            form = SearchUserForm()
        return render(request, 'main/search_user_forgp.html', {'form': form})
    else:
        return render(request, 'main/custom.html', {'not_member': 'you are not member of this group',})


@login_required
def remove_user(request, user_id, group_id):
    group = get_object_or_404(Group, id=group_id)
    user = get_object_or_404(User, id=user_id)
    if user in group.member.all() and user != group.admin:
        group = group.member.remove(user)
    elif user == group.admin:
        return render(request, 'main/custom.html', {'not_removable': 'you can\'t remove admin',
                                                    'not_removable_gp': group})
    else:
        return redirect('account:dashboard')
    return render(request, 'main/remove_user.html', {'user': user, 'group': group})

@login_required
def create_group_task(request, id):
    group = get_object_or_404(Group, id=id)
    if request.user in group.member.all() or request.user == group.admin:
        if request.method == 'POST':
            user = request.user
            create_form = GroupTaskCreateForm(request.POST)
            if create_form.is_valid():
                group_task = GroupTask(group=group,
                                      user=user,
                                      text=create_form.cleaned_data['text'],
                                      done=create_form.cleaned_data['done'])
                group_task.save()
                return redirect('main:group_detail', id=group.id)
        else:
            create_form = GroupTaskCreateForm()
        return render(request, 'main/create_group_task.html', {'form': create_form})
    else:
        return render(request, 'main/custom.html', {'not_member': 'you are not member of this group',})
# TODO: when member who is admin too, left the group, should remove from admin field
