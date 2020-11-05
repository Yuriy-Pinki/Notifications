from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class Task(models.Model):

    title = models.CharField('Task title', max_length=100)
    description = models.TextField('Description of title')
    create_datetime = models.DateTimeField('creating date and time')

    
    def __str__(self):
        return self.title

class Notification(models.Model):
    class NotificationUrgency(models.TextChoices):
        MINOR = 'Minor', _('Minor')
        MAJOR = 'Major', _('Major')
        CRITICAL = 'Critical', _('Critical')

    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    notification_datetime = models.DateTimeField('notification date and time')
    urgency = models.CharField(max_length=20, 
        choices = NotificationUrgency.choices, 
        default = NotificationUrgency.MINOR, )