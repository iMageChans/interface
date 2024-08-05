from base.actions import BaseActionsRead
from amm.service.read import Read
from utils.JSONExtractor import extractor
from amm.celery.update_or_created_celery import update_or_created_token_market_information
from amm.serializers import TokenMarketInformationSerializer


class GetReserves(BaseActionsRead):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        read = Read(self.keypair).get_reserves()
        data = extractor.d9_to_usdt(read.value_serialized)
        self.results = update_or_created_token_market_information(data)

    def serializers(self):
        return TokenMarketInformationSerializer(self.results).data

    def is_success(self):
        if self.results is None:
            return False
        return True

