from django.urls import path
from . import views
app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create_task/', views.create_task, name='create_task'),
    path('edit_task/<int:id>/', views.edit_task, name='single_task'),
    path('groups/', views.group_list, name='group_list'),
    path('group/<int:id>/', views.group_detail, name='group'),
]
