from main_mining.service.read import Read
from users_profile.serializers import *
from utils.JSONExtractor import extractor
from utils.keystone import *


def update_or_create_burning_profile(account_id, keypair):
    valid_keypair = check_keypair(keypair)

    valid_address = ValidAddress(account_id)

    data = {
        "account_id": valid_address.mate_data_address()
    }

    main_read = Read(valid_keypair)
    res = main_read.get_portfolio(valid_address.get_valid_address())
    data.update(extractor.get_burning_portfolio(res.value_serialized))

    user_burning_profile, created = UserBurningProfile.objects.update_or_create(
        account_id=data['account_id'],
        defaults=data
    )
    print({"account_id": user_burning_profile.account_id, "data": data, "created": created})
    return user_burning_profile
