from base.actions import BaseActionsRead
from votings.service.read import Read
from utils.keystone import ValidAddress


class ValidatorStats(BaseActionsRead):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        validator_id = ValidAddress(validated_data['validator_id'])
        self.results = Read().validator_stats(validator_id=validator_id.get_valid_address())

    def serializers(self):
        return self.results

    def is_success(self):
        return True
