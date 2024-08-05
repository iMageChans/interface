from base.actions import BaseActionsRead
from votings.service.read import Read


class GetNumberOfCandidates(BaseActionsRead):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.results = Read().get_number_of_candidates()

    def serializers(self):
        return self.results - 4

    def is_success(self):
        return True
