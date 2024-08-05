from base.actions import BaseActionsRead
from usdt.service.read import Read
from utils.JSONExtractor import extractor
from utils import numbers


class TotalSupply(BaseActionsRead):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.results = Read(self.keypair).total_supply()

    def serializers(self):
        values = numbers.format_usdt(extractor.get_data_or_err(self.results.value_serialized))
        return values
