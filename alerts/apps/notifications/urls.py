from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:task_id>/', views.detail, name='task'),
 #   path('<int:task_id>/detail/', views.task, name='results'),
    ]