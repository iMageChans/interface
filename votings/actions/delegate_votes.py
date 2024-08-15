from base.actions import BaseActionsExec
from votings.service.exec import Exec
from utils.keystone import ValidAddress


class DelegateVotes(BaseActionsExec):
    def __init__(self, validated_data):
        super().__init__(validated_data)

        candidate = ValidAddress(validated_data['candidate'])

        delegations = {
            "candidate": candidate.get_valid_address(),
            "amount": validated_data['amount'],
        }

        voting = Exec()
        delegations_voting = voting.delegate_votes(delegations=delegations)
        nonce = voting.d9_interface.get_account_nonce(account_address=self.keypair.ss58_address)
        self.extrinsic = voting.d9_interface.create_signed_extrinsic(call=delegations_voting,
                                                                     keypair=self.keypair,
                                                                     nonce=nonce)
        self.results = voting.d9_interface.submit_extrinsic(self.extrinsic,
                                                            wait_for_inclusion=True)

    def serializers(self):
        return self.extrinsic.value_serialized

    def is_success(self):
        return True
    