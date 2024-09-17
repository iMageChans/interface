from urllib.parse import urlparse

from dogpile.cache import make_region
from django_redis import get_redis_connection
from substrateinterface import SubstrateInterface

from base.config import PYTHON_MAIN_NET_URL
from interface import settings

redis_cache = settings.CACHES.get('default')

if redis_cache and 'redis' in redis_cache['BACKEND'].lower():
    redis_location = redis_cache['LOCATION']

    # 解析 Redis 的连接 URL
    parsed_redis_url = urlparse(redis_location)

    redis_host = parsed_redis_url.hostname or 'localhost'
    redis_port = parsed_redis_url.port or 6379
    redis_db = int(parsed_redis_url.path.lstrip('/')) if parsed_redis_url.path else 0
    redis_password = parsed_redis_url.password or None

    # 配置 dogpile.cache 的缓存区域，使用 Redis 作为后端，不包含 SSL 配置
    region = make_region().configure(
        'dogpile.cache.redis',
        expiration_time=3600,
        arguments={
            'host': redis_host,
            'port': redis_port,
            'db': redis_db,
            'password': redis_password,
        }
    )
else:
    # 如果没有配置 Redis，使用内存缓存作为默认选项
    region = make_region().configure(
        'dogpile.cache.memory',
        expiration_time=3600,
    )

ws_options = {
    'ping_interval': 30,
    'ping_timeout': 10,
    'connection_timeout': 20,
    'max_size': 2 ** 23,  # 8MB
    'read_limit': 2 ** 23,
    'write_limit': 2 ** 23,
}


class D9PalletsExec:
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
