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


class D9Contract:

    def __init__(self, contract_address: str, metadata_file: str, keypair: Keypair):
        self.contract = ContractInstance.create_from_address(
            contract_address=contract_address,
            metadata_file=metadata_file,
            substrate=D9Interface(
                url=MAIN_NET_URL,
                cache_region=region,
                auto_discover=True,
                auto_reconnect=True,
            ),
        )

        self.keypair = keypair

    def contract_exec(self, call_name: str, call_params: dict | None = None, value: int = 0):
        return self.contract.exec(self.keypair, call_name, call_params, value)

    def contract_read(self, call_name: str, call_params: dict | None = None, value: int = 0):
        return self.contract.read(self.keypair, call_name, call_params, value)
