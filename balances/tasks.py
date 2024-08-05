from celery import shared_task
from users_profile.celery.update_or_created_d9_balance import update_or_create_d9_balance


@shared_task
def update_or_create_d9_balance_celery(account_id):
    d9_balance = update_or_create_d9_balance(account_id=account_id)
    print({"account_id": account_id, "d9_balance": d9_balance})
    return d9_balance
