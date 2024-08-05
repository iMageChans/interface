from base.actions import BaseActionsExec
from votings.service.exec import Exec


class AddVotingInterest(BaseActionsExec):
    def __init__(self, validated_data):
        super().__init__(validated_data)

        voting = Exec()
        add_voting = voting.add_voting_interest(beneficiary_voter=self.account_id.get_valid_address(),
                                                amount_to_burn=validated_data['amount_to_burn'])
        nonce = voting.d9_interface.get_account_nonce(account_address=self.keypair.ss58_address)
        self.extrinsic = voting.d9_interface.create_signed_extrinsic(call=add_voting,
                                                                     keypair=self.keypair,
                                                                     nonce=nonce)
        self.results = voting.d9_interface.submit_extrinsic(self.extrinsic,
                                                            wait_for_inclusion=True)
