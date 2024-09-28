from balances.service.read import Read
from users_profile.serializers import *
from utils import numbers
from utils.JSONExtractor import JSONExtractor
from utils.keystone import ValidAddress


def update_or_create_d9_balance(account_id):
    valid_address = ValidAddress(account_id)

    data = {
        "account_id": valid_address.mate_data_address()
    }

    balances_read = Read()
    res = balances_read.get_balances(account_id=valid_address.get_valid_address())
    data.update({"balance_d9": numbers.DecimalTruncation(4).format_d9(JSONExtractor().get_balances_d9(res))})

    try:
        user_balance = UserBalances.objects.get(account_id=valid_address.mate_data_address())
        if user_balance.balance_d9 != str(JSONExtractor().get_balances_d9(res)):
            user_balance, created = UserBalances.objects.update_or_create(
                account_id=data['account_id'],
                defaults=data
            )
        return UserBalancesSerializer(user_balance).data
    except UserBalances.DoesNotExist:
        user_balance, created = UserBalances.objects.update_or_create(
            account_id=data['account_id'],
            defaults=data
        )
        return UserBalancesSerializer(user_balance).data



