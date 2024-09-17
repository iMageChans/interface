from urllib.parse import urlparse

from dogpile.cache import make_region
from substrateinterface import SubstrateInterface
from base.config import PYTHON_MAIN_NET_URL

region = make_region().configure(
    'dogpile.cache.memory',
    expiration_time=3600,
)


class D9PalletsExec:
    def __init__(self, pallet_name: str):
        self.substrate = SubstrateInterface(
            url=PYTHON_MAIN_NET_URL,
            ss58_format=9,
            type_registry_preset='polkadot',
            auto_discover=False,
            use_remote_preset=False,
            auto_reconnect=True,
            cache_region=region,
        )
        self.d9_interface = self.substrate

        self.pallet_name = pallet_name

    def compose_call(self, function_name: str, function_params: dict | None = None):
        return self.d9_interface.compose_call(
            call_module=self.pallet_name,
            call_function=function_name,
            call_params=function_params
        )


class D9PalletsRead:
    def __init__(self, pallet_name: str):
        self.substrate = SubstrateInterface(
            url=PYTHON_MAIN_NET_URL,
            ss58_format=9,
            type_registry_preset='polkadot',
            auto_discover=False,
            use_remote_preset=False,
            auto_reconnect=True,
            ws_options=ws_options,
            cache_region=region,
        )
        self.d9_interface = self.substrate
        self.pallet_name = pallet_name

    def compose_query(self, function_name: str, function_params: list):
        return self.d9_interface.query(
            module=self.pallet_name,
            storage_function=function_name,
            params=function_params
        )
