from django.db import models
from django.utils.translation import gettext_lazy as _

class Task(models.Model):

    title = models.CharField('Заголовок задачи', max_length=100)
    description = models.TextField('Текст задачи')
    create_datetime = models.DateTimeField('Дата создания задачи')

    
    def __str__(self):
        return self.task_title

class Notification(models.Model):
    class NotificationUrgency(models.TextChoices):
        MINOR = 'Minor', _('Minor')
        MAJOR = 'Major', _('Major')
        CRITICAL = 'Critical', _('Critical')

    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    notification_datetime = models.DateTimeField('Время и дата уведомления для задачи')
    urgency = models.CharField(max_length=20, 
        choices = NotificationUrgency.choices, 
        default = NotificationUrgency.MINOR, )

