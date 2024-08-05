from base.actions import BaseActionsExec
from usdt.service.exec import Exec
from utils import numbers


class BurnMiningAllowance(BaseActionsExec):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.results = Exec(self.keypair).burn_mining_allowance(
            amount=numbers.to_usdt(validated_data['amount']),
        )