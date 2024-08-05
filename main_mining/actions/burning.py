from base.actions import BaseActionsExec
from main_mining.service.exec import Exec
from utils import numbers
from main_mining.tasks import *
from balances.tasks import *


class Burning(BaseActionsExec):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        amount = numbers.to_d9(validated_data['amount'])
        self.results = Exec(self.keypair).burning(self.account_id.get_valid_address(), amount)

        user_burning_profile = update_or_create_user_burning_profile_celery.delay(
            account_id=self.account_id.mate_data_address(),
            keypair=self.keypair.private_key.hex())
        d9_balance = update_or_create_d9_balance_celery.delay(account_id=self.account_id.mate_data_address())
