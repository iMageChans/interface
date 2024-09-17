from base.actions import BaseActionsExec
from usdt.service.exec import Exec
from utils import numbers
from utils.keystone import ValidAddress


class Approve(BaseActionsExec):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        to_address = ValidAddress(validated_data['to_address'])
        self.results = Exec(self.keypair).approve(
            spender=to_address.get_valid_address(),
            amount=numbers.to_usdt(validated_data['amount']),
        )

    def serializers(self):
        return self.results.value_serialized

    def is_success(self):
        return True
