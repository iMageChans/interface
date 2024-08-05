from base.actions import BaseActionsRead
from amm.service.read import Read
from utils import numbers


class CheckUSDTBalance(BaseActionsRead):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.results = Read(self.keypair).check_usdt_balance(
            account_id=self.account_id.get_valid_address(),
            usdt_amount=numbers.to_usdt(validated_data['amount'])
        )