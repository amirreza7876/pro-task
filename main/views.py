from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import re

class IndexView(TemplateView):
    template_name = 'main/index.html'

@login_required
def team_register(request):
    user = request.user
    if not user.team_creator.all():
        if request.method == 'POST':
            team_form = CompanyCreateForm(request.POST)
            if team_form.is_valid():
                new_team = team_form.save(commit=False)
                new_team.creator = request.user
                new_team.save()
                team = Team.objects.get(id=new_team.id)
                team.member.add(user)
                return render(request, 'main/team_detail.html', {'team': team})
        else:
            team_form = CompanyCreateForm()
    else:
        messages.error(request,'you already have a team')
        return redirect('main:team_detail', user.team_creator.get().id)
        # return render(request, 'main/company_detail.html', {'error': 'error'})
    return render(request, 'main/company_registration.html', {'form':team_form})

@login_required
def team_detail(request, id):
    team = get_object_or_404(Team, id=id)
    if request.user in team.member.all():
            return render(request, 'main/team_detail.html', {'team': team})
    elif request.user not in team.member.all():
        if request.method == 'POST':
            join_form = MemberJoinForm(request.POST)
            if join_form.is_valid():
                form = join_form.cleaned_data
                if form['secret_key'] == team.secret_key:
                    team.member.add(request.user)
                    return redirect('main:team_detail', id=team.id)
                else:
                    return redirect('account:dashboard')
        else:
            join_form = MemberJoinForm()
    return render(request, 'main/join_to_co.html', {'form': join_form})


@login_required
def add_member(request, id):
    token_generator = default_token_generator
    print(token_generator)
    team = get_object_or_404(Team, id=id)
    if request.user in team.member.all() or request.user == team.creator:
        if request.method == 'POST':
            form = SearchUserForm(request.POST)
            if form.is_valid():
                list_name = form.cleaned_data['usern']
                usernames = re.sub('[^\w]', ' ', list_name).split()
                user_not_found = []
                user_exists = []
                user_added = []

                for username in usernames:
                    try:
                        user = User.objects.get(username=username)
                        if user in team.member.all():
                            user_exists.append(username)
                        elif user not in team.member.all():
                            # team.member.add(user)
                            user.offers.create(text='{} wants you to join to {} team in WWW.EXAMPLE.COM\
                                                    if you want to accept this invitation click on bellow\
                                                    link....'.format(request.user, team.name),
                                               from_user=request.user,
                                               team=request.user.team_creator.get())
                            user_added.append(username)
                        team.save()
                    except ObjectDoesNotExist as not_found:
                        user_not_found.append(username)
                return render(request, 'main/search_user_forgp.html',
                              {'form': form,
                              'team': team,
                              'user_not_found': user_not_found,
                              'success_users': username,
                              'user_exists': user_exists,
                              'user_added': user_added})
                # group.save()
                return redirect('main:team_detail', id=team.id)
        else:
            form = SearchUserForm()
            return render(request, 'main/search_user_forgp.html', {'form': form,'team':team})
    else:
        return render(request, 'main/custom.html', {'not_member': 'you are not member of this team',})

@login_required
def show_offers(request):
    user = request.user
    offers = user.offers.all()
    return render(request, 'main/show_offers.html', {'offers': offers})


@login_required
def accept_invite(request, id):
    team = get_object_or_404(Team, id=id)
    user = request.user
    # if user.is_authenticated:
    if user not in team.member.all():
        team.member.add(user)
        team.save()
        offers_from_one_team = Request.objects.filter(team=user.workat.get())
        for offer in offers_from_one_team:
            offer.delete()
        # user.offers.from_user.team_creator.get().id.remove()
        return redirect('main:team_detail', team.id)
    else:
        messages.error(request,'you already have a team')
        return redirect('main:team_detail', team.id)



# def accept_invitation(request,)
#
#
# @login_required
# def remove_user(request, user_id, group_id):
#     group = get_object_or_404(Group, id=group_id)
#     user = get_object_or_404(User, id=user_id)
#     if user in group.member.all() and user != group.admin:
#         group = group.member.remove(user)
#     elif user == group.admin:
#         return render(request, 'main/custom.html', {'not_removable': 'you can\'t remove admin',
#                                                     'not_removable_gp': group})
#     else:
#         return redirect('account:dashboard')
#     return render(request, 'main/remove_user.html', {'user': user, 'group': group})
#
# @login_required
# def create_group_task(request, id):
#     group = get_object_or_404(Group, id=id)
#     if request.user in group.member.all() or request.user == group.admin:
#         if request.method == 'POST':
#             user = request.user
#             create_form = GroupTaskCreateForm(request.POST)
#             if create_form.is_valid():
#                 group_task = GroupTask(group=group,
#                                       user=user,
#                                       text=create_form.cleaned_data['text'],
#                                       done=create_form.cleaned_data['done'])
#                 group_task.save()
#                 return redirect('main:group_detail', id=group.id)
#         else:
#             create_form = GroupTaskCreateForm()
#         return render(request, 'main/create_group_task.html', {'form': create_form})
#     else:
#         return render(request, 'main/custom.html', {'not_member': 'you are not member of this group',})
#TODO: when member who is admin too, left the group, should remove from admin field
#
#
#
# @login_required
# def group_create(request):
#     if request.user.co_own.all():
#         if request.method == 'POST':
#             form = CoGroupCreateForm(request.POST)
#             if form.is_valid:
#                 new_group = form.save(commit=False)
#                 new_group.admin = request.user
#                 new_group.save()
#                 group = Group.objects.get(id=new_group.id)
#                 group.member.add(request.user)
#                 return render(request, 'main/group_created.html', {'group': new_group})
#         else:
#             form = CoGroupCreateForm()
#     else:
#         return redirect('main:company_register')
#     return render(request, 'main/register_group.html', {'form': form})
#
#
# @login_required
# def group_detail(request, id):
#     group = get_object_or_404(Group, id=id)
#     tasks = group.tasks.all()
#     return render(request, 'main/group_detail.html', {'group': group, 'tasks': tasks})
#
#
# @login_required
# def user_groups(request):
#     user = request.user
#     groups = user.groups_in.all()
#
#     return render(request, 'main/user_groups_in.html', {'user': user,
#                                                         'groups': groups})
#
# @login_required
# def user_teams(request):
#     user = request.user
#     teams_in = user.workat.all()
#     return render(request, 'main/user_teams_in.html', {'user': user,
#                                                         'teams': teams_in})
# @login_required
# def create_task(request):
#     if request.method == 'POST':
#         user = request.user
#         create_form = CreateTaskForm(request.POST)
#         if create_form.is_valid():
#             new_post = SingleTask(user=user,
#                                   text=create_form.cleaned_data['text'],
#                                   done=create_form.cleaned_data['done'])
#             new_post.save()
#             return redirect('account:profile_detail', username=user.username,)
#     else:
#         create_form = CreateTaskForm()
#     return render(request, 'main/create_task.html', {'form': create_form})
#
#
# @login_required
# # @permission_required ??
# def edit_task(request, id):
#     task = get_object_or_404(SingleTask,id=id, user=request.user)
#     user = request.user
#     if request.method == 'POST':
#         edit_form = EditTaskForm(request.POST)
#         if edit_form.is_valid():
#             task.text = edit_form.cleaned_data['text']
#             task.done = edit_form.cleaned_data['done']
#             task.save()
#             return redirect('account:profile_detail',username=user.username)
#     else:
#         edit_form = EditTaskForm()
#     return render(request, 'main/edit_task.html', {'task': task,
#                                                    'form': edit_form})
