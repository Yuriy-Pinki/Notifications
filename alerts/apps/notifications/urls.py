from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:task_id>/', views.detail, name='detail'),
    path('add_task/', views.add_task, name='add_task'),
    path('<int:task_id>/detete_task/', views.delete_task, name='delete_task'),
    path('<int:task_id>/edit_task/', views.edit_task, name='edit_task'),
    ]