from celery import shared_task
from users_profile import celery


@shared_task
def update_or_create_user_burning_profile_celery(account_id, keypair):
    user_burning_profile = celery.update_or_create_burning_profile(account_id=account_id, keypair=keypair)
    print({"account_id": account_id, "user_burning_profile": user_burning_profile})
    return user_burning_profile
