from substrateinterface.contracts import ContractExecutionReceipt

from base.d9_contracts import D9Contract
from substrateinterface import Keypair
from base import config
from main_mining.abi import files


class Exec(D9Contract):

    def __init__(self, keypair: Keypair):
        super().__init__(
            contract_address=config.MAIN_MINING_CONTRACT,
            metadata_file=files.get_abi_files(),
            keypair=keypair
        )

    def burning(self, account_id: str, amount: int) -> ContractExecutionReceipt:
        params = {
            "burn_beneficiary": account_id,
            "burn_contract": config.BURN_MINING_CONTRACT
        }
        return self.contract_exec('burn', params, value=amount)

    def withdraw(self) -> ContractExecutionReceipt:
        params = {
            "burn_contract": config.BURN_MINING_CONTRACT,
        }
        return self.contract_exec('withdraw', params)