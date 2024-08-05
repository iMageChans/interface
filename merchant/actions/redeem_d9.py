from base.actions import BaseActionsExec
from merchant.service.exec import Exec
from balances.tasks import update_or_create_d9_balance_celery


class RedeemD9(BaseActionsExec):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.results = Exec(self.keypair).redeem_d9()
        d9_balance = update_or_create_d9_balance_celery.delay(self.account_id.mate_data_address())
