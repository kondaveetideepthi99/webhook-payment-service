import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webhook_payment_service.settings')

app = Celery('webhook_payment_service')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()  # this discovers tasks.py in each app

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
