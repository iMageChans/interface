from base.actions import BaseActionsExec
from node_reward.service.exec import Exec
from utils.keystone import ValidAddress


class WithdrawReward(BaseActionsExec):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        node_id = ValidAddress(validated_data['node_id'])
        self.results = Exec(self.keypair).withdraw_reward(node_id=node_id.get_valid_address())
