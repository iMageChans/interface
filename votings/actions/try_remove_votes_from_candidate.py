from base.actions import BaseActionsExec
from users_profile.models import UserToNodeVote
from votings.service.exec import Exec
from votings.service.read import Read
from utils.keystone import ValidAddress


class TryRemoveVotesFromCandidate(BaseActionsExec):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.node_id = ValidAddress(validated_data['node_id'])
        voting = Exec()
        add_voting = voting.try_remove_votes_from_candidate(candidate=self.node_id.get_valid_address(),
                                                            votes=validated_data['votes'])
        nonce = voting.d9_interface.get_account_nonce(account_address=self.keypair.ss58_address)
        self.extrinsic = voting.d9_interface.create_signed_extrinsic(call=add_voting,
                                                                     keypair=self.keypair,
                                                                     nonce=nonce)
        self.results = voting.d9_interface.submit_extrinsic(self.extrinsic,
                                                            wait_for_inclusion=True)

        if self.results.is_success:
            node_metadata = Read().get_node_metadata(node_id=self.node_id.get_valid_address())
            node_to_user_vote = Read().node_to_user_vote_totals(node_id=self.node_id.get_valid_address())
            for user in node_to_user_vote:
                data = {
                    "node_id": "Dn" + self.node_id.mate_data_address(),
                    "node_name": node_metadata['name'],
                    "account_id": f"Dn{user[0]}",
                    "vote": user[1]
                }

                UserToNodeVote.objects.update_or_create(
                    account_id=data["account_id"],
                    node_id=data["node_id"],
                    defaults=data
                )