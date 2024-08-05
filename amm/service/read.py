from scalecodec.types import GenericContractExecResult

from base.d9_contracts import D9Contract
from substrateinterface import Keypair
from base import config
from amm.abi import files


class Read(D9Contract):

    def __init__(self, keypair: Keypair):
        super().__init__(
            contract_address=config.MARKET_MAKER_CONTRACT,
            metadata_file=files.get_abi_files(),
            keypair=keypair
        )

    def get_reserves(self):
        return self.contract_read('get_currency_reserves')

    def get_liquidity_provider(self, account_id: str) -> GenericContractExecResult:
        params = {
            "account_id": account_id,
        }
        return self.contract_read('get_liquidity_provider', params)

    def check_new_liquidity(self, usdt_liquidity: int, d9_liquidity: int)  -> GenericContractExecResult:
        params = {
            "usdt_liquidity": usdt_liquidity,
            "d9_liquidity": d9_liquidity
        }
        return self.contract_read('check_new_liquidity', params)

    def calculate_exchange(self, direction, from_amount: int) -> GenericContractExecResult:
        params = {
            "direction": direction,
            "amount_0": from_amount
        }
        return self.contract_read('calculate_exchange', params)

    def estimate_exchange(self, direction, from_amount: int) -> GenericContractExecResult:
        params = {
            "direction": direction,
            "amount_0": from_amount
        }
        return self.contract_read('estimate_exchange', params)

    def check_usdt_balance(self, account_id: str, usdt_amount: int) -> GenericContractExecResult:
        params = {
            "account_id": account_id,
            "amount": usdt_amount
        }
        return self.contract_read('check_usdt_balance', params)