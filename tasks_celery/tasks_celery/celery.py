from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
import logging


logger = logging.getLogger("Celery")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tasks_celery.settings")
app = Celery('mydjango')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.taks(bind=True)
def debu_task(self):
    print(f"Request: {self.request}")
