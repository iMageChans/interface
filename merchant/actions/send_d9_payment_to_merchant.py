from base.actions import BaseActionsExec
from merchant.service.exec import Exec
from utils.keystone import ValidAddress
from utils.numbers import *
from balances.tasks import update_or_create_d9_balance_celery


class SendD9PaymentToMerchant(BaseActionsExec):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.merchant_id = ValidAddress(validated_data['merchant_id'])
        self.results = Exec(self.keypair).send_d9_payment_to_merchant(self.merchant_id.get_valid_address(),
                                                                      to_d9(validated_data['amount']))

        d9_balance = update_or_create_d9_balance_celery.delay(self.merchant_id.mate_data_address())

        merchant_balance = update_or_create_d9_balance_celery.delay(self.merchant_id.mate_data_address())
