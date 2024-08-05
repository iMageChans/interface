from substrateinterface.contracts import ContractExecutionReceipt

from base.d9_contracts import D9Contract
from substrateinterface import Keypair
from base import config
from node_reward.abi import files


class Exec(D9Contract):

    def __init__(self, keypair: Keypair):
        super().__init__(
            contract_address=config.NODE_REWARD_CONTRACT,
            metadata_file=files.get_abi_files(),
            keypair=keypair
        )

    def withdraw_reward(self, node_id: str) -> ContractExecutionReceipt:
        params = {
            "node_id": node_id,
        }
        return self.contract_exec('withdraw_reward', params)