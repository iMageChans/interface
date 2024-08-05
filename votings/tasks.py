from celery import shared_task
from votings.celery.update_or_created_node_user_vote import update_or_created_node_user_vote
from votings.celery.update_or_created_rank import update_or_created_rank


@shared_task
def update_or_created_node_user_vote_celery():
    update_or_created_node_user_vote()


@shared_task
def get_rank():
    update_or_created_rank()
