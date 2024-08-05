from base.actions import BaseActionsExec
from usdt.service.exec import Exec
from utils import numbers


class DecreaseAllowance(BaseActionsExec):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.results = Exec(self.keypair).decrease_allowance(
            spender=self.account_id.get_valid_address(),
            amount=numbers.to_usdt(validated_data['amount']),
        )
