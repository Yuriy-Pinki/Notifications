from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseNotFound
from .models import Task, Notification
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse 
from datetime import datetime

from .forms import NotyForm

def index(request):
	task_list = Task.objects.order_by('-create_datetime')
	context = {'task_list': task_list}
	return render(request,'notifications/index.html', context)

def detail(request, task_id):
	task = get_object_or_404(Task, pk=task_id)
	return render(request, 'notifications/detail.html', {'task':task})

def add_task(request):
	a = Task.objects.create(title=request.POST['task_title'], \
		description=request.POST['task_description'], \
		create_datetime=datetime.now())
	date = request.POST['date']
	time = request.POST['time']
	set_datetime = str(date) + ' ' + str(time)
	a.notification_set.create(urgency=request.POST['select_urgency'],\
		notification_datetime=set_datetime)
	return HttpResponseRedirect(reverse('notifications:index'))

def delete_task(request, task_id):
	task = Task.objects.get(pk=task_id)
	task.delete()
	return HttpResponseRedirect(reverse('notifications:index'))
	
def edit_task(request, task_id):
	try:
		task = get_object_or_404(Task, pk=task_id)

		if request.method == "POST":
			task.title = request.POST["task_title"]
			task.description = request.POST["task_description"]
			task.save()
			return render(request, "notifications/detail.html", {'task':task})
		else:
			return render(request, "notifications/edit.html", {'task':task})
	except Task.DoesNotExist:
		return HttpResponseNotFound("<h2>Task not found</h2>")
