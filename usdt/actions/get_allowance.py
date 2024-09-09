from base.actions import BaseActionsRead
from usdt.service.read import Read


class GetAllowance(BaseActionsRead):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        usdt_read = Read(self.keypair)
        self.results = usdt_read.get_allowance(owner=self.account_id.get_valid_address())

    def serializers(self):
        return self.results.value_serialized

    def is_success(self):
        return True