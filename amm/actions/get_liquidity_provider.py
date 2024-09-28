from base.actions import BaseActionsRead
from amm.service.read import Read
from utils.JSONExtractor import JSONExtractor


class GetLiquidityProvider(BaseActionsRead):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.results = Read(self.keypair).get_liquidity_provider(self.account_id.get_valid_address())

    def serializers(self):
        return JSONExtractor().get_data_or_err(self.results.value_serialized)

    def is_success(self):
        if self.results is None:
            return False
        return True
