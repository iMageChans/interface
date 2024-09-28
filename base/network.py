from typing import Any, Dict, List, Optional, Union
from substrateinterface.exceptions import SubstrateRequestException

from base.config import PYTHON_MAIN_NET_URL
from substrateinterface.contracts import ContractInstance
from substrateinterface import Keypair, SubstrateInterface
from dogpile.cache import make_region
from typing import Optional

import logging

# 配置日志记录
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


region = make_region().configure(
    'dogpile.cache.memory',
    expiration_time=3600,
)


class D9Contract:
    def __init__(self, contract_address: str, metadata_file: str, keypair: Keypair):
        self.keypair = keypair
        self.substrate = substrate = SubstrateInterface(
            url=PYTHON_MAIN_NET_URL,
            ss58_format=9,
            type_registry_preset='polkadot',
            auto_discover=False,
            use_remote_preset=False,
            auto_reconnect=True,
            cache_region=region,
        )
        self.contract = ContractInstance.create_from_address(
            contract_address=contract_address,
            metadata_file=metadata_file,
            substrate=self.substrate,
        )

    def get_block_number(self, block_hash: str) -> int:
        """
        Get the block number for the given block hash.

        Parameters:
            block_hash (str): The hash of the block.

        Returns:
            int: The block number.
        """
        return self.contract.substrate.get_block_number(block_hash=block_hash)

    def contract_exec(
            self,
            call_name: str,
            call_params: Optional[dict] = None,
            value: int = 0
    ):
        """
        Execute a contract function that alters the contract state.

        Parameters:
            call_name (str): The name of the contract function to call.
            call_params (Optional[dict]): The parameters for the function call.
            value (int): The value to transfer when executing the call.

        Returns:
            Execution result.
        """
        result = self.contract.exec(self.keypair, call_name, call_params, value)
        return result

    def contract_read(
            self,
            call_name: str,
            call_params: Optional[dict] = None,
            value: int = 0
    ):
        """
        Read data from the contract without altering its state.

        Parameters:
            call_name (str): The name of the contract function to call.
            call_params (Optional[dict]): The parameters for the function call.
            value (int): The value to transfer when reading the call.

        Returns:
            Reading result.
        """
        result = self.contract.read(self.keypair, call_name, call_params, value)
        return result


class D9Pallets:
    """
    Base class providing an interface to Substrate nodes and cache configuration.
    """

    def __init__(self, pallet_name: str):
        """
        Initialize the SubstrateInterface and specify the pallet name.

        :param pallet_name: The name of the pallet (module) to interact with.
        """
        self.pallet_name = pallet_name
        try:
            self.substrate = SubstrateInterface(
                url=PYTHON_MAIN_NET_URL,
                ss58_format=9,
                type_registry_preset='polkadot',
                auto_discover=False,
                use_remote_preset=False,
                auto_reconnect=True,
                cache_region=region,
            )
            logger.info(f"Successfully connected to Substrate node: {PYTHON_MAIN_NET_URL}")
        except Exception as e:
            logger.error(f"Failed to connect to Substrate node: {e}")
            raise ConnectionError(f"Failed to connect to Substrate node: {e}") from e

    def compose_call(self, function_name: str, function_params: Optional[Dict[str, Any]] = None):
        """
        Compose a transaction call.

        :param function_name: The name of the function to call.
        :param function_params: A dictionary of function parameters.
        :return: The composed call object.
        """
        try:
            call = self.substrate.compose_call(
                call_module=self.pallet_name,
                call_function=function_name,
                call_params=function_params or {}
            )
            logger.debug(f"Successfully composed call: {function_name} with params {function_params}")
            return call
        except Exception as e:
            logger.error(f"Failed to compose call: {e}")
            raise ValueError(f"Failed to compose call: {e}") from e

    def compose_query(self, function_name: str, function_params: Optional[List[Any]] = None):
        """
        Compose a query call.

        :param function_name: The name of the query function to call.
        :param function_params: A list of parameters for the query function.
        :return: The query result.
        """
        try:
            result = self.substrate.query(
                module=self.pallet_name,
                storage_function=function_name,
                params=function_params or []
            )
            logger.debug(f"Query successful: {function_name} with params {function_params}")
            return result
        except SubstrateRequestException as e:
            logger.error(f"Query failed: {e}")
            raise ValueError(f"Query failed: {e}") from e
        except Exception as e:
            logger.error(f"Unknown error: {e}")
            raise RuntimeError(f"Unknown error: {e}") from e


