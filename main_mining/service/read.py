from scalecodec.types import GenericContractExecResult

from base.d9_contracts import D9Contract
from substrateinterface import Keypair
from base import config
from main_mining.abi import files


class Read(D9Contract):

    def __init__(self, keypair: Keypair):
        super().__init__(
            contract_address=config.MAIN_MINING_CONTRACT,
            metadata_file=files.get_abi_files(),
            keypair=keypair
        )

    def get_total_burned(self) -> GenericContractExecResult:
        return self.contract_read('get_total_burned')

    def get_portfolio(self, account_id: str) -> GenericContractExecResult:
        params = {
            "account_id": account_id,
        }
        return self.contract_read('get_portfolio', params)