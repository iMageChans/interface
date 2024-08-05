from base.actions import BaseActionsExec
from merchant.service.exec import Exec
from utils.keystone import ValidAddress
from utils.numbers import *
from balances.tasks import update_or_create_d9_balance_celery
from merchant.tasks import update_or_created_get_user_merchant_profile_celery


class GivePointsD9(BaseActionsExec):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.consumer_id = ValidAddress(validated_data['consumer_id'])
        self.results = Exec(self.keypair).give_points_d9(self.consumer_id.get_valid_address(),
                                                         to_d9(validated_data['amount']))

        d9_balance = update_or_create_d9_balance_celery.delay(self.account_id.mate_data_address())
        user_merchant_profile = update_or_created_get_user_merchant_profile_celery.delay(
            self.consumer_id.mate_data_address(),
            self.keypair.private_key.hex())
