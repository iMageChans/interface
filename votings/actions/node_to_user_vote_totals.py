from base.actions import BaseActionsRead
from votings.service.read import Read
from utils.keystone import ValidAddress


class NodeToUserVoteTotals(BaseActionsRead):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        node_id = ValidAddress(validated_data['node_id'])
        user_id = validated_data.get('user_id', None)
        if user_id is None:
            node_user_vote_list = list()
            reads = Read().node_to_user_vote_totals(node_id=node_id.get_valid_address())
            for read in reads:
                data = {
                    "account_id": f"Dn{read[0]}",
                    "vote": read[1]
                }
                node_user_vote_list.append(data)
            self.results = node_user_vote_list
        else:
            valid_user_id = ValidAddress(user_id)
            self.results = Read().node_to_user_vote_totals(node_id=node_id.get_valid_address(),
                                                           user_id=valid_user_id.get_valid_address())

    def serializers(self):
        return self.results

    def is_success(self):
        return True
