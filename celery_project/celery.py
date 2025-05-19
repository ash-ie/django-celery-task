from __future__ import absolute_import,unicode_literals
from celery import Celery
from django.conf import settings
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','celery_project.settings')

app = Celery('celery_project')                      
app.conf.enable_utc = False
app.conf.update(timezone='Asia/Kolkata')
app.config_from_object('django.conf:settings', namespace='CELERY')

#celery Beat settings
app.conf.beat_schedule = {

}

app.autodiscover_tasks()
@app.task(blind=True)
def debug_task(self):
    print(f'Request:{self.request!r}')
