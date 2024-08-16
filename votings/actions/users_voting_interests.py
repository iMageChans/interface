from base.actions import BaseActionsRead
from votings.service.read import Read


class UsersVotingInterests(BaseActionsRead):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.results = Read().users_voting_interests(account_id=self.account_id.get_valid_address())

    def serializers(self):
        return self.results

    def is_success(self):
        return True