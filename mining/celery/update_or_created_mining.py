from substrateinterface import Keypair
from mining.service.read import Read
from utils.JSONExtractor import JSONExtractor
from mining.models import *
from users_profile.celery.update_or_created_d9_balance import update_or_create_d9_balance


def update_or_created_all_volume():
    mnemonic = Keypair.generate_mnemonic()
    keypair = Keypair.create_from_mnemonic(mnemonic)
    read = Read(keypair)
    accumulative_reward_pool_rsp = read.get_accumulative_reward_pool()
    merchant_volume_rsp = read.get_merchant_volume()
    total_volume_rsp = read.get_total_volume()
    session_volume_rsp = read.get_session_volume(session_index=1)

    accumulative_reward_pool_res = JSONExtractor().get_data_or_err(accumulative_reward_pool_rsp.value_serialized)
    merchant_volume_res = JSONExtractor().get_data_or_err(merchant_volume_rsp.value_serialized)
    total_volume_res = JSONExtractor().get_data_or_err(total_volume_rsp.value_serialized)
    session_volume_res = JSONExtractor().get_data_or_err(session_volume_rsp.value_serialized)

    accumulative_reward_pool = AccumulativeRewardPool.objects.order_by('-created_at').first()
    merchant_volume = MerchantVolume.objects.order_by('-created_at').first()
    total_volume = TotalVolume.objects.order_by('-created_at').first()
    session_volume = SessionVolume.objects.order_by('-created_at').first()

    if accumulative_reward_pool:
        accumulative_reward_pool.totals = accumulative_reward_pool_res
        accumulative_reward_pool.save()
    else:
        accumulative_reward_pool = AccumulativeRewardPool.objects.create(totals=accumulative_reward_pool_res)

    if merchant_volume:
        merchant_volume.totals = merchant_volume_res
        merchant_volume.save()
    else:
        merchant_volume = MerchantVolume.objects.create(totals=merchant_volume_res)

    if total_volume:
        total_volume.totals = total_volume_res
        total_volume.save()
    else:
        total_volume = TotalVolume.objects.create(totals=total_volume_res)

    if session_volume:
        session_volume.totals = session_volume_res
        session_volume.save()
    else:
        session_volume = SessionVolume.objects.create(totals=session_volume_res)

    address_list = ["DnwRGYShktZsxtKwXCCzqtLW7P1a5K2qDsaXEcRWxVYKGwH7d",
                    "DnzXB3VPHrnb9pzfJweLstBfmn5Xq3dEAFAbKKxTsQZg1entq"]

    for address in address_list:
        balance = update_or_create_d9_balance(account_id=address)
