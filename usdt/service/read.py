from scalecodec.types import GenericContractExecResult

from base.d9_contracts import D9Contract
from substrateinterface import Keypair
from base import config
from usdt.abi import files


class Read(D9Contract):

    def __init__(self, keypair: Keypair):
        super().__init__(
            contract_address=config.USDT_CONTRACT,
            metadata_file=files.get_abi_files(),
            keypair=keypair
        )

    def balance_of(self, owner: str) -> GenericContractExecResult:
        return self.contract_read('PSP22::balance_of', {'owner': owner})

    def total_supply(self) -> GenericContractExecResult:
        return self.contract_read('PSP22::total_supply')

    def get_allowance(self, owner: str, spender: str) -> GenericContractExecResult:
        return self.contract_read('PSP22::allowance', {'owner': owner, 'spender': spender})