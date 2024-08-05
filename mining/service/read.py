from scalecodec.types import GenericContractExecResult

from base.d9_contracts import D9Contract
from substrateinterface import Keypair
from base import config
from mining.abi import files


class Read(D9Contract):

    def __init__(self, keypair: Keypair):
        super().__init__(
            contract_address=config.NEW_MINING_CONTRACT,
            metadata_file=files.get_abi_files(),
            keypair=keypair
        )

    def get_accumulative_reward_pool(self):
        return self.contract_read('get_accumulative_reward_pool')

    def get_merchant_volume(self):
        return self.contract_read('get_merchant_volume')

    def get_session_volume(self, session_index: int):
        params = {
            "session_index": session_index,
        }
        return self.contract_read('get_session_volume', params)

    def get_total_volume(self):
        return self.contract_read('get_total_volume')