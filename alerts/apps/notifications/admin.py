from django.contrib import admin

from .models import Task, Notification

admin.site.register(Task)
admin.site.register(Notification)
