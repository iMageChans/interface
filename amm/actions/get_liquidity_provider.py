from base.actions import BaseActionsRead
from amm.service.read import Read
from utils.JSONExtractor import extractor


class GetLiquidityProvider(BaseActionsRead):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.results = Read(self.keypair).get_liquidity_provider(self.account_id.get_valid_address())

    def serializers(self):
        if len(self.results.value_serialized) <= 0:
            return self.results.value_serialized
        return extractor.d9_to_usdt(self.results.value_serialized)