from celery import shared_task
from merchant import celery


@shared_task
def update_or_created_get_merchant_expiry_celery(account_id, keypair):
    merchant_expiry = celery.update_or_created_get_merchant_expiry(account_id=account_id, keypair=keypair)
    print({"account_id": account_id, "merchant_expiry": merchant_expiry})
    return merchant_expiry


@shared_task
def update_or_created_get_user_merchant_profile_celery(account_id, keypair):
    user_merchant_profile = celery.update_or_created_get_user_merchant_profile(account_id=account_id, keypair=keypair)
    print({"account_id": account_id, "user_merchant_profile": user_merchant_profile})
    return user_merchant_profile