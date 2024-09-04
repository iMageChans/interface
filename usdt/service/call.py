from scalecodec.types import GenericContractExecResult

from base.d9_contracts import D9Contract
from substrateinterface import Keypair
from base import config
from usdt.abi import files


class Call(D9Contract):

    def __init__(self, keypair: Keypair):
        super().__init__(
            contract_address=config.USDT_CONTRACT,
            metadata_file=files.get_abi_files(),
            keypair=keypair
        )

    def balance_of(self, owner: str) -> GenericContractExecResult:
        return self.contract_call('PSP22::balance_of', {'owner': owner})

    def total_supply(self) -> GenericContractExecResult:
        return self.contract_call('PSP22::total_supply')