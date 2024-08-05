from substrateinterface.contracts import ContractExecutionReceipt

from base.d9_contracts import D9Contract
from substrateinterface import Keypair
from base import config
from amm.abi import files


class Exec(D9Contract):

    def __init__(self, keypair: Keypair):
        super().__init__(
            contract_address=config.MARKET_MAKER_CONTRACT,
            metadata_file=files.get_abi_files(),
            keypair=keypair
        )

    def add_liquidity(self, usdt_amount: int, d9_amount: int) -> ContractExecutionReceipt:
        params = {
            "usdt_liquidity": usdt_amount,
        }
        return self.contract_exec('add_liquidity', params, value=d9_amount)

    def remove_liquidity(self) -> ContractExecutionReceipt:
        return self.contract_exec('remove_liquidity')

    def get_d9(self, usdt: int) -> ContractExecutionReceipt:
        params = {
            "usdt": usdt
        }
        return self.contract_exec('get_d9', params)

    def get_usdt(self, d9_amount: int) -> ContractExecutionReceipt:
        return self.contract_exec('get_usdt', value=d9_amount)