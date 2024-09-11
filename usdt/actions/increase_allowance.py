from base.actions import BaseActionsExec
from usdt.service.exec import Exec
from utils import numbers
from utils.keystone import ValidAddress


class IncreaseAllowance(BaseActionsExec):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.to_address = ValidAddress(validated_data['to_address'])
        self.results = Exec(self.keypair).increase_allowance(
            spender=self.to_address.get_valid_address(),
            amount=numbers.to_usdt(validated_data['amount']),
        )
