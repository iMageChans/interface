from base.actions import BaseActionsExec
from merchant.service.exec import Exec
from merchant.tasks import update_or_created_get_merchant_expiry_celery
from usdt.tasks import update_or_create_usdt_balance_celery


class Subscribe(BaseActionsExec):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.results = Exec(self.keypair).subscribe(validated_data['usdt_base_units'])
        usdt_balance = update_or_create_usdt_balance_celery.delay(self.account_id.mate_data_address(),
                                                                  self.keypair.private_key.hex())
        merchant_expiry = update_or_created_get_merchant_expiry_celery.delay(self.account_id.mate_data_address(),
                                                                             self.keypair.private_key.hex())
