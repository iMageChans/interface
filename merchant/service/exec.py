from substrateinterface.contracts import ContractExecutionReceipt

from base.d9_contracts import D9Contract
from substrateinterface import Keypair
from base import config
from merchant.abi import files


class Exec(D9Contract):

    def __init__(self, keypair: Keypair):
        super().__init__(
            contract_address=config.MERCHANT_CONTRACT,
            metadata_file=files.get_abi_files(),
            keypair=keypair
        )

    def subscribe(self, usdt_base_units: int) -> ContractExecutionReceipt:
        params = {
            "usdt_amount": usdt_base_units,
        }
        return self.contract_exec('subscribe', params)

    def redeem_d9(self) -> ContractExecutionReceipt:
        return self.contract_exec('redeem_d9')

    def give_points_d9(self, consumer_id: str, amount: int) -> ContractExecutionReceipt:
        params = {
            "consumer_id": consumer_id,
        }
        return self.contract_exec('give_green_points_d9', params, value=amount)

    def give_points_usdt(self, consumer_id: str, amount: int) -> ContractExecutionReceipt:
        params = {
            "consumer_id": consumer_id,
            "usdt_amount": amount
        }
        return self.contract_exec('give_green_points_usdt', params, value=amount)

    def send_usdt_payment_to_merchant(self, merchant_id: str, amount: int) -> ContractExecutionReceipt:
        params = {
            "merchant_id": merchant_id,
            "usdt_amount": amount
        }
        return self.contract_exec('send_usdt_payment_to_merchant', params, value=amount)

    def send_d9_payment_to_merchant(self, merchant_id: str, amount: int) -> ContractExecutionReceipt:
        params = {
            "merchant_id": merchant_id,
        }
        return self.contract_exec('send_d9_payment_to_merchant', params, value=amount)
