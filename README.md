#### Common
* Adding git file and db.sqlite3 to the *.gitignore* `Notification`
* Run `python manage.py makemigrations notifications`
* Run `python manage.py migrate`
* add `Task` model to the admin panel
* deleting git file
* adding `Notification` model to the admin panel
* 
***
#### models.py
* Adding the class named `Notification`
* Adding params `models.ForeignKey` into the `Notification` in models.py
* Editing ENUM according to the Django Documentation
* deleting some spaces in *notifications/models.py*
* rewriting *notifications/models.py* only in English
* editing the magic method
```
    def __str__(self):
        return self.title
```
***
#### views.py
* adding to *notification/views.py* `index` view function
* adding `index`  view (show tasklist)
* adding `detail` view with `try\except` construction (show details of something task)
* adding `add_task` view
* adding creating task and notifications to him
***
#### settings.py 
* set `en_US` language in *settings.py*
* Adding `Notifications` app *settings.py*
```
INSTALLED_APPS = [
'notifications.apps.NotificationsConfig',]
```
****
#### HTML templates
* adding *index.html*
move *alerts/templates/notifications/index.html* to *alerts/apps/notifications/templates/notifications/*
* adding `detail.html`. It shows details of particular task
* adding `html form` for creating new task
* editing `html form` to correct show
* some visual changes in `detail.html`