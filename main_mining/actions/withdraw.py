from base.actions import BaseActionsExec
from main_mining.service.exec import Exec
from main_mining.tasks import *
from balances.tasks import *


class Withdraw(BaseActionsExec):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.results = Exec(self.keypair).withdraw()

        user_burning_profile = update_or_create_user_burning_profile_celery.delay(
            account_id=self.account_id.mate_data_address(),
            keypair=self.keypair.private_key.hex())
        d9_balance = update_or_create_d9_balance_celery.delay(account_id=self.account_id.mate_data_address())