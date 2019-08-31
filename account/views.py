from django.shortcuts import render, get_object_or_404
from .models import User
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from common.decorators import ajax_required
from .models import Contact
from main.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm


@ajax_required
@require_POST
@login_required
def user_follow(request):
    user_id = request.POST.get('id')
    action = request.POST.get('action')
    if user_id and action:
        try:
            user = User.objects.get(id=user_id)
            if action == 'follow':
                Contact.objects.get_or_create(user_from=request.user, user_to=user)
            else:
                Contact.objects.filter(user_from=request.user, user_to=user).delete()
            return JsonResponse({'status': 'ok'})
        except User.DoesNotExist:
            return JsonResponse({'status': 'ko'})
    return JsonResponse({'status': 'ko'})


@login_required
def profile_detail(request, username):
    user = get_object_or_404(User, username=username)
    tasks = SingleTask.objects.filter(active=True, user=user)

    context = {
        'tasks': tasks,
        'this_user': user,
        'section': 'people',
    }
    return render(request, 'account/user/detail.html', context)

def profile_list(request):
    users = User.objects.all()
    context = {
        'users': users,
        'section': 'people'
    }
    return render(request, 'account/user/list.html', context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'],
                                         password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('login successful')
                else:
                    return HttpResponse('disabled account')
            else:
                return HttpResponse('invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/reg_success.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()

    return render(request, 'account/register.html', {'user_form':user_form})
