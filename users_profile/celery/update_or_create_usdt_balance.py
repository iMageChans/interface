from usdt.service.read import Read
from users_profile.serializers import *
from utils import numbers
from utils.JSONExtractor import JSONExtractor
from utils.keystone import *


def update_or_create_usdt_balance(account_id, keypair):
    valid_address = ValidAddress(account_id)
    valid_keypair = check_keypair(keypair)

    data = {
        "account_id": valid_address.mate_data_address()
    }

    usdt_read = Read(valid_keypair)
    res = usdt_read.balance_of(owner=valid_address.get_valid_address())
    data.update({"balance_usdt": numbers
                .DecimalTruncation(2)
                .format_usdt(JSONExtractor().get_data_or_err(res.value_serialized))})

    try:
        usdt_balance = USDTBalances.objects.get(account_id=valid_address.mate_data_address())
        if usdt_balance.balance_usdt != str(JSONExtractor().get_data_or_err(res.value_serialized)):
            usdt_balance, created = USDTBalances.objects.update_or_create(
                account_id=data['account_id'],
                defaults=data
            )
        return USDTBalancesSerializer(usdt_balance).data
    except USDTBalances.DoesNotExist:
        usdt_balance, created = USDTBalances.objects.update_or_create(
            account_id=data['account_id'],
            defaults=data
        )
        return USDTBalancesSerializer(usdt_balance).data
