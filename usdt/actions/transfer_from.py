from base.actions import BaseActionsExec
from usdt.service.exec import Exec
from utils import numbers
from utils.keystone import ValidAddress
from usdt.tasks import update_or_create_usdt_balance_celery


class TransferFrom(BaseActionsExec):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.from_address = ValidAddress(validated_data['from_address'])
        self.to_address = ValidAddress(validated_data['to_address'])
        self.results = Exec(self.keypair).transfer_from(
            from_address=self.from_address.get_valid_address(),
            to_address=self.to_address.get_valid_address(),
            amount=numbers.to_usdt(validated_data['amount']),
        )

        transfer_form = update_or_create_usdt_balance_celery.delay(self.from_address.mate_data_address(),
                                                                   self.keypair.private_key.hex())
        to_form = update_or_create_usdt_balance_celery.delay(self.to_address.mate_data_address(),
                                                             self.keypair.private_key.hex())
