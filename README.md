* Добавление класса `Notification`
* Добавление параметра `models.ForeignKey` в класс `Notification`

 	`INSTALLED_APPS = [
    'notifications.apps.NotificationsConfig',`

* Редактирование перечистений ENUM в соответствии с документацией Django
* Запуск команды python manage.py makemigrations notifications
	log
	`Migrations for 'notifications':
  alerts\apps\notifications\migrations\0001_initial.py
    - Create model Task
    - Create model Notification`

* python manage.py migrate   >> OK