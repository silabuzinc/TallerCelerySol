# djangoApp/celery.py

import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoTemplates.settings")
app = Celery("DjangoTemplates")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()