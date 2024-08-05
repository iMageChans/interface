from scalecodec.types import GenericContractExecResult

from base.d9_contracts import D9Contract
from substrateinterface import Keypair
from base import config
from node_reward.abi import files


class Read(D9Contract):

    def __init__(self, keypair: Keypair):
        super().__init__(
            contract_address=config.NODE_REWARD_CONTRACT,
            metadata_file=files.get_abi_files(),
            keypair=keypair
        )

    def get_vote_limit(self) -> GenericContractExecResult:
        return self.contract_read('get_vote_limit')

    def get_node_rewards_data(self, node_id: str) -> GenericContractExecResult:
        params = {
            "node_id": node_id,
        }
        return self.contract_read('get_node_reward_data', params)