from scalecodec.types import GenericCall
from tomlkit import value

from base.d9_interfaces import D9Interface
from base.config import *

from substrateinterface.contracts import ContractInstance
from substrateinterface import Keypair

from dogpile.cache import make_region
from django_redis import get_redis_connection

from typing import Optional


redis_connection = get_redis_connection('default')

region = make_region().configure(
    'dogpile.cache.memory',
    expiration_time=3600,
)


class D9Contract:

    def __init__(self, contract_address: str, metadata_file: str, keypair: Keypair):
        self.contract = ContractInstance.create_from_address(
            contract_address=contract_address,
            metadata_file=metadata_file,
            substrate=D9Interface(
                # url="https://mainnet.d9network.com:40200",
                url=MAIN_NET_URL,
                cache_region=region,
                auto_discover=True,
                auto_reconnect=True,
            ),
        )

        self.keypair = keypair

    def get_block_numbers(self, block_hash: str) -> int:
        return self.contract.substrate.get_block_number(block_hash=block_hash)

    def contract_exec(self, call_name: str, call_params: dict | None = None, value: int = 0):
        return self.contract.exec(self.keypair, call_name, call_params, value)

    def contract_read(self, call_name: str, call_params: dict | None = None, value: int = 0):
        return self.contract.read(self.keypair, call_name, call_params, value)

    def contract_call(self, call_name: str, call_params: dict | None = None, value: int = 0):
        return self.call(self.keypair, call_name, call_params, value)

    def contract_get_payment_info(self, call_name: str, call_params: dict | None = None, value: int = 0):
        return self.get_payment_info(self.keypair, call_name, call_params, value)

    def get_payment_info(self, keypair: Keypair, method: str, args: dict = None,
             value: int = 0, gas_limit: Optional[dict] = None, storage_deposit_limit: int = None
             ):

        if gas_limit is None:
            gas_predit_result = self.contract.read(keypair, method, args, value)
            gas_limit = gas_predit_result.gas_required

        input_data = self.contract.metadata.generate_message_data(name=method, args=args)

        call = self.contract.substrate.compose_call(
            call_module='Contracts',
            call_function='call',
            call_params={
                'dest': self.contract.contract_address,
                'value': value,
                'gas_limit': gas_limit,
                'storage_deposit_limit': storage_deposit_limit,
                'data': input_data.to_hex()
            }
        )

        return self.contract.substrate.get_payment_info(call=call, keypair=keypair)

    def call(self, keypair: Keypair, method: str, args: dict = None, value: int = 0, gas_limit: Optional[dict] = None, storage_deposit_limit: int = None) -> GenericCall:
        input_data = self.contract.metadata.generate_message_data(name=method, args=args)
        return self.contract.substrate.compose_call(
            call_module='Contracts',
            call_function='call',
            call_params={
                'dest': self.contract.contract_address,
                'value': value,
                'gas_limit': gas_limit,
                'storage_deposit_limit': storage_deposit_limit,
                'data': input_data.to_hex()
            }
        )
