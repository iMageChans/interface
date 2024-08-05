from base.actions import BaseActionsRead
from votings.service.read import Read


class GetSessionNodeList(BaseActionsRead):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.results = Read().get_session_node_list(session_index=validated_data['session_index'])

    def serializers(self):
        return self.results

    def is_success(self):
        return True
