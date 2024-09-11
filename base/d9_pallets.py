from base.d9_interfaces import D9Interface
from base.config import *

from substrateinterface.contracts import ContractInstance
from substrateinterface import Keypair

from dogpile.cache import make_region
from django_redis import get_redis_connection

redis_connection = get_redis_connection('default')

region = make_region().configure(
    'dogpile.cache.memory',
    expiration_time=3600,
)


class D9PalletsExec:
    def __init__(self, pallet_name: str):
        self.d9_interface = D9Interface(
            url=PYTHON_MAIN_NET_URL,
            ss58_format=9,
            type_registry_preset='polkadot',
            cache_region=region,
        )

        self.pallet_name = pallet_name

    def compose_call(self, function_name: str, function_params: dict | None = None):
        return self.d9_interface.compose_call(
            call_module=self.pallet_name,
            call_function=function_name,
            call_params=function_params
        )


class D9PalletsRead:
    def __init__(self, pallet_name: str):
        self.d9_interface = D9Interface(
            url=PYTHON_MAIN_NET_URL,
            ss58_format=9,
            type_registry_preset='polkadot',
            cache_region=region,
        )
        self.pallet_name = pallet_name

    def compose_query(self, function_name: str, function_params: list):
        return self.d9_interface.query(
            module=self.pallet_name,
            storage_function=function_name,
            params=function_params
        )