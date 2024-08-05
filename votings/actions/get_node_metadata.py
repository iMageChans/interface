from base.actions import BaseActionsRead
from votings.service.read import Read
from utils.keystone import ValidAddress


class GetNodeMetaData(BaseActionsRead):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        node_id = ValidAddress(validated_data['node_id'])
        self.results = Read().get_node_metadata(node_id=node_id.get_valid_address())

    def serializers(self):
        return self.results

    def is_success(self):
        return True