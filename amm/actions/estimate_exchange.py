from base.actions import BaseActionsRead
from amm.service.read import Read
from utils.numbers import to_number
from utils.JSONExtractor import JSONExtractor


class EstimateExchange(BaseActionsRead):
    def __init__(self, validated_data):
        super().__init__(validated_data)

        self.from_currency = validated_data['from_currency']
        self.to_currency = validated_data['to_currency']

        if self.from_currency == "USDT" and self.to_currency == "D9":
            from_amount = to_number(validated_data['from_amount'], 2)
        else:
            from_amount = to_number(validated_data['from_amount'])

        self.results = Read(self.keypair).estimate_exchange(
            direction=[self.from_currency, self.to_currency],
            from_amount=from_amount
        )

    def serializers(self):
        if self.from_currency == "USDT" and self.to_currency == "D9":

            return {
                "rate": JSONExtractor().estimate_exchange_rate_usdt_to_d9(self.results.value_serialized),
                "meta_data": JSONExtractor().usdt_to_d9(self.results.value_serialized)
            }
        else:

            return {
                "rate": JSONExtractor().estimate_exchange_rate_d9_to_usdt(self.results.value_serialized),
                "meta_data": JSONExtractor().d9_to_usdt(self.results.value_serialized)
            }
