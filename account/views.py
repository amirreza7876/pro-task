from django.shortcuts import render, get_object_or_404, redirect
from .models import User
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from common.decorators import ajax_required
# from .models import Contact
from main.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm


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


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'],
                                         password=cd['password'])
            if user is not None:
                if user.is_active:
                    # if not user.team_creator.all():
                    #     login(request, user)
                    #     if user.is_authenticated:
                    #         return redirect('main:team_register')

                    login(request, user)
                    return redirect('main:index')
                else:
                    return HttpResponse('disabled account')
            else:
                return render(request, 'account/login.html', {'form': form,
                                                              'invalid_login': 'invalid'})
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

# TODO: change team register place from login to register ...
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            if new_user:
                login(request, new_user)
                return redirect('main:team_register')

            # return render(request, 'account/reg_success.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form':user_form})


@login_required
def dashboard(request):
    # groups = user.groups_in.all()
    # followings = user.following.all()[:10]
    # followers = user.followers.all()[:10]
    user = request.user
    return render(request, 'account/user/dashboard.html', {'user': user,})
    if user.workat.get() or user.team_creator.get():
        team_in = user.workat.get()
        team_creator = user.team_creator.get()
        return render(request, 'account/user/dashboard.html', {'user': user,
                                                               'team': team_in,
                                                               # 'team_own': team,
                                                               'team_creator': team_creator
                                                               # 'groups': groups,
                                                                # 'followings': followings,
                                                                # 'followers': followers,
                                                                })
#
#
# @login_required
# def user_followers(request):
#     user = request.user
#     followers = user.followers.all()
#     return render(request, 'account/user/followers.html', {'followers': followers})
#
#
# def user_followings(request):
#     user = request.user
#     followings = user.following.all()[:10]
#     return render(request, 'account/user/followings.html', {'followings': followings})
#
#
# @ajax_required
# @require_POST
# @login_required
# def user_follow(request):
#     user_id = request.POST.get('id')
#     action = request.POST.get('action')
#     if user_id and action:
#         try:
#             user = User.objects.get(id=user_id)
#             if action == 'follow':
#                 Contact.objects.get_or_create(user_from=request.user, user_to=user)
#             else:
#                 Contact.objects.filter(user_from=request.user, user_to=user).delete()
#             return JsonResponse({'status': 'ok'})
#         except User.DoesNotExist:
