from base.actions import BaseActionsRead
from utils.token_rate_calculation import *
from utils.numbers import DecimalTruncation


class ComputeExchangeRate(BaseActionsRead):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.from_currency = validated_data['from_currency']
        self.to_currency = validated_data['to_currency']
        self.results = get_currency_rate_amount(
            self.from_currency,
            self.to_currency,
            validated_data['from_amount']
        )

    def serializers(self):
        return {
            "rate": DecimalTruncation(2).truncate(self.results),
            "meta_data": self.results
        }

    def is_success(self):
        if self.results:
            return True
        return False
