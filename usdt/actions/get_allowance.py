from base.actions import BaseActionsRead
from usdt.service.read import Read
from utils import numbers
from utils.JSONExtractor import JSONExtractor
from utils.keystone import ValidAddress


class GetAllowance(BaseActionsRead):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        usdt_read = Read(self.keypair)
        from_address = ValidAddress(validated_data['from_address'])
        to_address = ValidAddress(validated_data['to_address'])
        self.results = usdt_read.get_allowance(owner=from_address.get_valid_address(), spender=to_address.get_valid_address())

    def serializers(self):
        return int(JSONExtractor().get_data_or_err(self.results.value_serialized)) / 100

    def is_success(self):
        return True