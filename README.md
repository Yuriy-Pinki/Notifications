* Adding the class named `Notification`
* Adding params `models.ForeignKey` into the `Notification`
`INSTALLED_APPS = [
'notifications.apps.NotificationsConfig',`

* Editing ENUM according to Django Documentation
* Run python manage.py makemigrations notifications
	log
	`Migrations for 'notifications':
  alerts\apps\notifications\migrations\0001_initial.py
    - Create model Task
    - Create model Notification`

* python manage.py migrate   >> OK
* Adding git file and db.sqlite3 to the .gitignore
* deliting some spaces