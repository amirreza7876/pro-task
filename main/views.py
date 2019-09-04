from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required, permission_required
from .models import *
from .forms import *
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
    return render(request, 'main/company_detail.html', {'company': company})


@login_required
def group_create(request):
    if request.user.co_own.all():
        if request.method == 'POST':
            form = CoGroupCreateForm(request.POST)
            if form.is_valid:
                new_group = form.save(commit=False)
                new_group.admin = request.user
                new_group.save()

                
                group = CompanyGroup.objects.get(id=new_group.id)
                group.member.add(request.user)
                return render(request, 'main/group_created.html', {'group': new_group})
        else:
            form = CoGroupCreateForm()
    else:
        return redirect('main:company_register')
    return render(request, 'main/register_group.html', {'form': form})


@login_required
def group_detail(request, id):
    group = get_object_or_404(CompanyGroup, id=id)
    return render(request, 'main/group_detail.html', {'group': group})
