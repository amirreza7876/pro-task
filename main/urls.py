from django.urls import path
from . import views
app_name = 'main'

urlpatterns = [
    # path('create-task/', views.create_task, name='create_task'),
    # path('edit-task/<int:id>/', views.edit_task, name='single_task'),
    # path('create/group/', views.group_create, name='group_create'),
    # path('mygroups/', views.user_groups, name='user_groups'),
    # path('group/<int:id>/', views.group_detail, name='group_detail'),
    path('', views.IndexView.as_view(), name='index'),
    path('register_team/', views.team_register, name='team_register'),
    path('team/<int:id>/', views.team_detail, name='team_detail'),
    # path('teams/', views.user_teams, name='user_teams'),
    path('add-member/group/<int:id>/', views.add_member, name='add_member'),
    path('offers/', views.show_offers, name='show_offers'),
    path('join/team/<int:id>/', views.accept_invite, name='accept_invite'),
    # path('create/group-task/<int:id>/', views.create_group_task, name='create_group_task'),
    # path('remove-member/<int:user_id>/group/<int:group_id>/', views.remove_user, name='remove_user')
]
