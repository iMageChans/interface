from base.actions import BaseActionsRead
from node_reward.service.read import Read
from utils.keystone import ValidAddress


class GetNodeRewardsData(BaseActionsRead):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        node_id = ValidAddress(validated_data['node_id'])
        self.results = Read(self.keypair).get_node_rewards_data(node_id=node_id.get_valid_address())
