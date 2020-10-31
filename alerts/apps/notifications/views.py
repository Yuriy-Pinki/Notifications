from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Task, Notification
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse 
from datetime import datetime

from .forms import NotyForm

def index(request):
	task_list = Task.objects.order_by('-create_datetime')

	if request.method == "POST":
		form = NotyForm(request.POST)
	else:
		form = NotyForm()

	context = {'task_list': task_list, 'form':form}
#	return render(request,'notifications/index.html', context)
	return render(request,'notifications/index.html', context)

def detail(request, task_id):
	try:
		task = Task.objects.get(pk=task_id)
	except Task.DoesNotExist:
		raise Http404("Task does not exist")
	return render(request, 'notifications/detail.html', {'task':task})

def add_task(request):
	a = Task.objects.create(title=request.POST['task_title'], \
		description=request.POST['task_description'], \
		create_datetime=datetime.now())
	date = request.POST['date']
	time = request.POST['time']
	set_datetime = str(date) + ' ' + str(time)
	a.notification_set.create(urgency=request.POST['select_urgency'], notification_datetime=set_datetime)
	return HttpResponseRedirect(reverse('notifications:index'))
