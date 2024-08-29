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

    def get_total_lp_tokens(self) -> GenericContractExecResult:
        return self.contract_read('get_total_lp_tokens')

    def get_reserves(self) -> GenericContractExecResult:
        return self.contract_read('get_currency_reserves')

    def get_liquidity_provider(self, account_id: str) -> GenericContractExecResult:
        params = {
            "account_id": account_id,
        }
        return self.contract_read('get_liquidity_provider', params)

    def check_new_liquidity(self, usdt_liquidity: int, d9_liquidity: int) -> GenericContractExecResult:
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

    def get_d9(self, usdt: int) -> GenericContractExecResult:
        params = {
            "usdt": usdt
        }
        return self.contract_read('get_d9', params)

    def get_usdt(self, d9_amount: int) -> GenericContractExecResult:
        return self.contract_read('get_usdt', value=d9_amount)

    def add_liquidity(self, usdt_amount: int, d9_amount: int) -> GenericContractExecResult:
        params = {
            "usdt_liquidity": usdt_amount,
        }
        return self.contract_read('add_liquidity', params, value=d9_amount)

    def remove_liquidity(self) -> GenericContractExecResult:
        return self.contract_read('remove_liquidity')