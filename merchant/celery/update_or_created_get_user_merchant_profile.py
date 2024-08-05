from users_profile.models import *
from merchant.service.read import Read
from utils.JSONExtractor import extractor
from utils.keystone import check_keypair, ValidAddress


def update_or_created_get_user_merchant_profile(account_id, keypair):
    valid_keypair = check_keypair(keypair)

    valid_address = ValidAddress(account_id)

    data = {
        "account_id": valid_address.mate_data_address()
    }

    merchant_read = Read(valid_keypair)
    res = merchant_read.get_user_merchant_profile(valid_address.get_valid_address())
    data.update(extractor.get_merchant_portfolio(res.value_serialized))

    user_merchant_profile, created = UserMerchantProfile.objects.update_or_create(
        account_id=data['account_id'],
        defaults=data
    )
    print({"account_id": user_merchant_profile.account_id, "created": created})
    return user_merchant_profile
