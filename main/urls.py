from django.urls import path
from . import views
app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create_task/', views.create_task, name='create_task'),
    path('edit_task/<int:id>/', views.edit_task, name='single_task'),
    path('register/co/', views.company_register, name='company_register'),
    path('company/<int:id>/', views.company_detail, name='company_detail'),
    path('create/group/', views.group_create, name='group_create'),
    path('group/<int:id>/', views.group_detail, name='group_detail'),

]
