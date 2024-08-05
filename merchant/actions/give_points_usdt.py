from base.actions import BaseActionsExec
from merchant.service.exec import Exec
from utils.keystone import ValidAddress
from utils.numbers import *
from usdt.tasks import update_or_create_usdt_balance_celery
from merchant.tasks import update_or_created_get_user_merchant_profile_celery


class GivePointsUSDT(BaseActionsExec):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.consumer_id = ValidAddress(validated_data['consumer_id'])
        self.results = Exec(self.keypair).give_points_usdt(self.consumer_id.get_valid_address(),
                                                           to_usdt(validated_data['amount']))

        usdt_balance = update_or_create_usdt_balance_celery.delay(self.account_id.mate_data_address(),
                                                                  self.keypair.private_key.hex())
        user_merchant_profile = update_or_created_get_user_merchant_profile_celery.delay(
            self.consumer_id.mate_data_address(),
            self.keypair.private_key.hex())
