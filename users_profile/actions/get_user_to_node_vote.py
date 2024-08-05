from base.actions import BaseActionsRead
from users_profile.serializers import *


class GetUserToNodeVote(BaseActionsRead):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        user_to_node_vote = UserToNodeVote.objects.filter(account_id=self.account_id.mate_data_address())
        self.results = UserToNodeVoteSerializer(user_to_node_vote, many=True).data

    def serializers(self):
        return self.results

    def is_success(self):
        return True
