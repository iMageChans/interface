from balances.service.read import Read
from base.actions import BaseActionsRead
from utils import numbers
from utils.JSONExtractor import JSONExtractor


class GetBalances(BaseActionsRead):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        balances_read = Read()
        self.results = balances_read.get_balances(account_id=self.account_id.get_valid_address())

    def serializers(self):
        return {"balance_d9": numbers.DecimalTruncation(4).format_d9(JSONExtractor().get_balances_d9(self.results))}

    def is_success(self):
        return True
