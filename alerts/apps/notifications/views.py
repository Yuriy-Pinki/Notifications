from django.http import HttpResponse, Http404
from .models import Task, Notification
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse 

def index(request):
	task_list = Task.objects.order_by('-create_datetime')
	context = {'task_list': task_list}
	return render(request,'notifications/index.html', context)

def detail(request, task_id):
	try:
		task = Task.objects.get(pk=task_id)
	except Task.DoesNotExist:
		raise Http404("Task does not exist")
	return render(request, 'notifications/detail.html', {'task':task})

def add_notification(request, task_id):
	a = Task.objects.get(id = task_id)
	a.notification_set.create(notification_datetime=request.POST['time'], urgency=request.POST['select_urgency'])
	return HttpResponseRedirect(reverse('notifications.detail', args=(a.id, )))
