from substrateinterface.contracts import ContractExecutionReceipt

from base.d9_contracts import D9Contract
from substrateinterface import Keypair
from base import config
from usdt.abi import files


class Exec(D9Contract):

    def __init__(self, keypair: Keypair):
        super().__init__(
            contract_address=config.USDT_CONTRACT,
            metadata_file=files.get_abi_files(),
            keypair=keypair
        )

    def approve(self, spender: str, amount: int):
        params = {
            "spender": spender,
            "value": amount
        }
        return self.contract_exec('PSP22::approve', params)

    def decrease_allowance(self, spender: str, amount: int):
        params = {
            "spender": spender,
            "delta_value": amount
        }
        return self.contract_exec('PSP22::decrease_allowance', params)

    def increase_allowance(self, spender: str, amount: int):
        params = {
            "spender": spender,
            "delta_value": amount
        }
        return self.contract_exec('PSP22::increase_allowance', params)

    def transfer(self, to_address: str, amount: int):
        params = {
            "to": to_address,
            "value": amount,
            "data": "0x"
        }
        return self.contract_exec('PSP22::transfer', params)

    def transfer_from(self, from_address: str, to_address: str, amount: int):
        params = {
            "from": from_address,
            "to": to_address,
            "value": amount,
            "data": "0x"
        }
        return self.contract_exec('PSP22::transfer_from', params)

    def node_reward_allowance(self, amount: int):
        params = {
            "spender": config.NODE_REWARD_CONTRACT,
            "value": amount
        }
        return self.contract_exec('PSP22::approve', params)

    def burn_mining_allowance(self, amount: int):
        params = {
            "spender": config.BURN_MINING_CONTRACT,
            "value": amount
        }
        return self.contract_exec('PSP22::approve', params)

    def main_mining_allowance(self, amount: int):
        params = {
            "spender": config.MAIN_MINING_CONTRACT,
            "value": amount
        }
        return self.contract_exec('PSP22::approve', params)

    def mining_allowance(self, amount: int):
        params = {
            "spender": config.NEW_MINING_CONTRACT,
            "value": amount
        }
        return self.contract_exec('PSP22::approve', params)

    def market_maker_allowance(self, amount: int):
        params = {
            "spender": config.MARKET_MAKER_CONTRACT,
            "value": amount
        }
        return self.contract_exec('PSP22::approve', params)

    def usdt_allowance(self, amount: int):
        params = {
            "spender": config.USDT_CONTRACT,
            "value": amount
        }
        return self.contract_exec('PSP22::approve', params)

    def merchant_allowance(self, amount: int):
        params = {
            "spender": config.MERCHANT_CONTRACT,
            "value": amount
        }
        return self.contract_exec('PSP22::approve', params)

    def cross_chain_allowance(self, amount: int):
        params = {
            "spender": config.CROSS_CHAIN_CONTRACT,
            "value": amount
        }
        return self.contract_exec('PSP22::approve', params)