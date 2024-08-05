from base.actions import BaseActionsExec
from usdt.service.exec import Exec
from utils import numbers


class MainMiningAllowance(BaseActionsExec):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.results = Exec(self.keypair).main_mining_allowance(
            amount=numbers.to_usdt(validated_data['amount']),
        )