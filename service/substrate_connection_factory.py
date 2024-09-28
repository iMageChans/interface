# substrate_connection_factory.py

from substrateinterface import SubstrateInterface
from dogpile.cache import make_region
from threading import Lock
import logging

# Configure logging
logger = logging.getLogger(__name__)

# Configure caching
region = make_region().configure(
    'dogpile.cache.memory',
    expiration_time=3600,
)

class SubstrateConnectionFactory:
    _instance = None
    _lock = Lock()

    def __init__(self, url: str, ss58_format: int, type_registry_preset: str):
        self.substrate = None
        try:
            self.substrate = SubstrateInterface(
                url=url,
                ss58_format=ss58_format,
                type_registry_preset=type_registry_preset,
                auto_discover=False,
                use_remote_preset=False,
                auto_reconnect=True,
                cache_region=region,
            )
            logger.info(f"Successfully connected to Substrate node: {url}")
        except Exception as e:
            logger.error(f"Failed to connect to Substrate node: {e}")
            raise ConnectionError(f"Failed to connect to Substrate node: {e}") from e

    @classmethod
    def get_instance(cls, url: str, ss58_format: int, type_registry_preset: str):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = cls(url, ss58_format, type_registry_preset)
        return cls._instance

    def get_substrate(self) -> SubstrateInterface:
        return self.substrate

    def get_contract_instance(self, contract_cls, keypair: Keypair):
        """
        Return an instance of the contract class, initialized with shared substrate.

        :param contract_cls: The contract class to instantiate.
        :param keypair: The keypair for the contract.
        :return: An instance of the contract class.
        """
        return contract_cls(keypair=keypair, substrate=self.substrate)
