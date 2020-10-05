#### Common
* Adding the class named `Notification`
* Adding params `models.ForeignKey` into the 
* Adding git file and db.sqlite3 to the *.gitignore* `Notification`
* Run `python manage.py makemigrations notifications`
* Run `python manage.py migrate`
* add `Task` field to the admin panel
* deleting git file
***
#### models.py
* Editing ENUM according to the Django Documentation
* deleting some spaces in *notifications/models.py*
* rewriting *notifications/models.py* only in English
***
#### views.py
* addint to *notification/views.py* `index` view function
***
#### settings.py 
* set `en_US` language in *settings.py*
* Adding our app *settings.py*
```>INSTALLED_APPS = [
'notifications.apps.NotificationsConfig',]
```
****
#### HTML templates
* adding *index.html*
* changing location of `index.html`, from *alerts/templates/notifications/* to *alerts/apps/notifications/templates/notifications/*
