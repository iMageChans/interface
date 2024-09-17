from base.actions import BaseActionsExec
from usdt.service.exec import Exec
from utils import numbers
from utils.keystone import ValidAddress


class DecreaseAllowance(BaseActionsExec):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        to_address = ValidAddress(validated_data['to_address'])
        self.results = Exec(self.keypair).decrease_allowance(
            spender=to_address.get_valid_address(),
            amount=numbers.to_usdt(validated_data['amount']),
        )
