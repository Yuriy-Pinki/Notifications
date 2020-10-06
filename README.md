#### Common
* Adding git file and db.sqlite3 to the *.gitignore* `Notification`
* Run `python manage.py makemigrations notifications`
* Run `python manage.py migrate`
* add `Task` model to the admin panel
* deleting git file
***
#### models.py
* Adding the class named `Notification`
* Adding params `models.ForeignKey` into the `Notification` in models.py
* Editing ENUM according to the Django Documentation
* deleting some spaces in *notifications/models.py*
* rewriting *notifications/models.py* only in English
***
#### views.py
* adding to *notification/views.py* `index` view function
***
#### settings.py 
* set `en_US` language in *settings.py*
* Adding our app *settings.py*
```
INSTALLED_APPS = [
'notifications.apps.NotificationsConfig',]
```
****
#### HTML templates
* adding *index.html*
move *alerts/templates/notifications/index.html* to *alerts/apps/notifications/templates/notifications/*
