from celery import shared_task
from users_profile.celery.update_or_create_usdt_balance import update_or_create_usdt_balance
from usdt.celery.update_or_created_currency_profile import update_or_created_currency_profile


@shared_task
def update_or_create_usdt_balance_celery(account_id, keypair):
    usdt_balance = update_or_create_usdt_balance(account_id=account_id, keypair=keypair)
    print({"account_id": account_id, "usdt_balance": usdt_balance})
    return usdt_balance


@shared_task
def update_or_created_currency_profile_celery():
    update_or_created_currency_profile()
