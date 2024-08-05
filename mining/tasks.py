from celery import shared_task
from mining.celery.update_or_created_mining import update_or_created_all_volume


@shared_task
def update_or_created_all_volume_celery():
    update_or_created_all_volume()
