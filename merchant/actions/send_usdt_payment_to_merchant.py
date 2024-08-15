from base.actions import BaseActionsExec
from merchant.service.exec import Exec
from utils.keystone import ValidAddress
from utils.numbers import *
from usdt.tasks import update_or_create_usdt_balance_celery


class SendUSDTPaymentToMerchant(BaseActionsExec):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.merchant_id = ValidAddress(validated_data['merchant_id'])
        self.results = Exec(self.keypair).send_usdt_payment_to_merchant(self.merchant_id.get_valid_address(),
                                                                        to_usdt(validated_data['amount']))

        usdt_balance = update_or_create_usdt_balance_celery.delay(self.merchant_id.mate_data_address(),
                                                                  self.keypair.private_key.hex())

        merchant_balance = update_or_create_usdt_balance_celery.delay(self.merchant_id.mate_data_address(),
                                                                      self.keypair.private_key.hex())
