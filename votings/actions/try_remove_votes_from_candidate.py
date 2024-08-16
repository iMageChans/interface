from base.actions import BaseActionsExec
from votings.service.exec import Exec
from utils.keystone import ValidAddress


class TryRemoveVotesFromCandidate(BaseActionsExec):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        node_id = ValidAddress(validated_data['node_id'])
        voting = Exec()
        add_voting = voting.try_remove_votes_from_candidate(candidate=node_id.get_valid_address(),
                                                            votes=validated_data['votes'])
        nonce = voting.d9_interface.get_account_nonce(account_address=self.keypair.ss58_address)
        self.extrinsic = voting.d9_interface.create_signed_extrinsic(call=add_voting,
                                                                     keypair=self.keypair,
                                                                     nonce=nonce)
        self.results = voting.d9_interface.submit_extrinsic(self.extrinsic,
                                                            wait_for_inclusion=True)