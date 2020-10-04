from django.http import HttpResponse
from .models import Task, Notification
from django.template import loader
from django.shortcuts import render

def index(request):
	task_list = Task.objects.order_by('-create_datetime')
	context = {'task_list': task_list}
	return render(request,'notifications/index.html', context)

def task(request):
	pass
