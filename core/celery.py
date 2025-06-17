import os
from celery import Celery
from celery.schedules import crontab # type: ignore

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

# Beat schedule (every minute)
app.conf.beat_schedule = {
    'send-welcome-email-every-minute': {
        'task': 'MyAPI.tasks.send_welcome_email',
        'schedule': 60.0,
    },
}
