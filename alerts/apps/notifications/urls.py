from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:task_id>/', views.detail, name='detail'),
    path('<int:task_id>/add_notification/', views.add_notification, name='add_notification'),
    ]