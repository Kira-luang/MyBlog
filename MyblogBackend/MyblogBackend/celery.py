import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyblogBackend.settings')
#　Django_rest_frame.settings -> 项目名.settings

app = Celery('MyblogBackend')  # settings所在目录名

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))