import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TaskBoard.settings')

app = Celery('TaskBoard')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'weekly_mail': {
        'task': 'TB.tasks.latest_news',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
    },
}