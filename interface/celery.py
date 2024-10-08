# web/celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'interface.settings')

app = Celery('interface')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'update_or_created_node_user_vote_celery': {
        'task': 'votings.tasks.update_or_created_node_user_vote_celery',
        'schedule': timedelta(seconds=60),
    },
    'get_rank': {
        'task': 'votings.tasks.get_rank',
        'schedule': timedelta(seconds=600),
    },
    'update_or_created_all_volume_celery': {
        'task': 'mining.tasks.update_or_created_all_volume_celery',
        'schedule': timedelta(seconds=300),
    },
    'update_or_created_currency_profile_celery': {
        'task': 'usdt.tasks.update_or_created_currency_profile_celery',
        'schedule': timedelta(seconds=600),
    },
    'update_or_created_token_market_information_celery': {
        'task': 'amm.tasks.update_or_created_token_market_information_celery',
        'schedule': timedelta(seconds=60),
    },
}
