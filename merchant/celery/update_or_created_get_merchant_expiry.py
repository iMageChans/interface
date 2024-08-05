from users_profile.models import *
from merchant.service.read import Read
from utils.JSONExtractor import extractor
from utils.keystone import check_keypair, ValidAddress


def update_or_created_get_merchant_expiry(account_id, keypair):
    valid_keypair = check_keypair(keypair)

    valid_address = ValidAddress(account_id)

    data = {
        "account_id": valid_address.mate_data_address()
    }

    merchant_read = Read(valid_keypair)
    res = merchant_read.get_merchant_expiry(valid_address.get_valid_address())
    data.update({"expiry_date": extractor.get_data_or_err(res.value_serialized)})

    merchant_expiry, created = MerchantExpiry.objects.update_or_create(
        account_id=data['account_id'],
        defaults=data
    )
    print({"account_id": merchant_expiry.account_id, "created": created})
    return merchant_expiry
