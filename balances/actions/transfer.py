from base.actions import BaseActionsExec
from balances.service.exec import Exec
from utils import numbers
from utils.keystone import ValidAddress
from utils.JSONExtractor import extractor
from balances.tasks import *


class Transfer(BaseActionsExec):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.to_address = ValidAddress(validated_data['to_address'])
        amount = numbers.to_d9(validated_data['amount'])

        balance = Exec()
        transfer = balance.transfer(recipient=self.to_address.get_valid_address(),
                                    amount=amount)

        nonce = balance.d9_interface.get_account_nonce(account_address=self.account_id.get_valid_address())
        self.extrinsic = balance.d9_interface.create_signed_extrinsic(call=transfer,
                                                                      keypair=self.keypair,
                                                                      nonce=nonce)

        self.results = balance.d9_interface.submit_extrinsic(self.extrinsic,
                                                             wait_for_inclusion=True)

        d9_balance_from = update_or_create_d9_balance_celery.delay(self.account_id.mate_data_address())
        d9_balance_to = update_or_create_d9_balance_celery.delay(self.to_address.mate_data_address())

    def serializers(self):
        return extractor.get_transfer_data(self.results)

    def is_success(self):
        return self.results.is_success
