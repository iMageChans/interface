from base.actions import BaseActionsRead
from node_reward.service.read import Read


class GetVoteLimit(BaseActionsRead):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.results = Read(self.keypair).get_vote_limit()
