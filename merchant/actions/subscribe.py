from base.actions import BaseActionsExec
from merchant.service.exec import Exec
from merchant.tasks import update_or_created_get_merchant_expiry_celery
from usdt.tasks import update_or_create_usdt_balance_celery
from utils.numbers import to_usdt


class Subscribe(BaseActionsExec):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.results = Exec(self.keypair).subscribe(usdt_base_units=to_usdt(validated_data['usdt_base_units']))
        usdt_balance = update_or_create_usdt_balance_celery.delay(self.account_id.mate_data_address(),
                                                                  self.keypair.private_key.hex())
        merchant_expiry = update_or_created_get_merchant_expiry_celery.delay(self.account_id.mate_data_address(),
                                                                             self.keypair.private_key.hex())

    def serializers(self):
        return self.results.value_serialized

    def is_success(self):
        return True
