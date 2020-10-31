from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:task_id>/', views.detail, name='detail'),
    path('add_task/', views.add_task, name='add_task'),
    ]