from base.actions import BaseActionsRead
from votings.service.read import Read


class CurrentSessionIndex(BaseActionsRead):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.results = Read().current_session_index()

    def serializers(self):
        return self.results

    def is_success(self):
        return True