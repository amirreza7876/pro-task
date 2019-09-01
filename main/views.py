from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required, permission_required
from .models import *
from .forms import CreateTaskForm, EditTaskForm, GroupJoinForm
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = 'main/index.html'


@login_required
def create_task(request):
    if request.method == 'POST':
        user = request.user
        print(user)
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


def group_list(request):
    groups = GroupTask.objects.filter(active=True)
    return render(request, 'main/group/list.html', {'groups': groups})


@login_required
def group_detail(request, id):
    group = get_object_or_404(GroupTask, id=id)
    if request.method == 'POST':
        if request.user != group.member:
            join_form = GroupJoinForm(request.POST)
            if join_form.is_valid():
                if join_form.cleaned_data['private_key'] == group.private_key:
                    group.member.add(request.user)
                    return redirect('main:group', id=group.id)
                else:
                    return redirect('main:group_list')
        else:
            return redirect('main:group', id=group.id)
    else:
        join_form = GroupJoinForm()
    return render(request, 'main/group/detail.html')
