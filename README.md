# django-celery-task
This is a demo project showcasing the working of Django Celery, Redis Base Setup

in one instance of the terminal run,

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

in anaother instance of the terminal run,

celery -A celery_project.celery:app worker --pool=solo -l info
