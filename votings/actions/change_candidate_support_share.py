from base.actions import BaseActionsExec
from votings.service.exec import Exec


class ChangeCandidateSupportShare(BaseActionsExec):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        voting = Exec()
        chang_name = voting.change_candidate_support_share(percent=validated_data['percent'])
        nonce = voting.d9_interface.get_account_nonce(account_address=self.keypair.ss58_address)
        self.extrinsic = voting.d9_interface.create_signed_extrinsic(call=chang_name,
                                                                     keypair=self.keypair,
                                                                     nonce=nonce)
        self.results = voting.d9_interface.submit_extrinsic(self.extrinsic,
                                                            wait_for_inclusion=True)
