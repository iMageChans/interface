# base/d9_pallets.py

import logging
from substrateinterface import SubstrateInterface
from typing import Any, Dict, Optional, List

logger = logging.getLogger(__name__)

class D9Pallets:
    def __init__(self, pallet_name: str, substrate: SubstrateInterface):
        self.pallet_name = pallet_name
        self.substrate = substrate
        logger.info(f"D9Pallets initialized with pallet: {pallet_name}")

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

    def query(self, function_name: str, params: Optional[List[Any]] = None):
        """
        Perform a query.

        :param function_name: The name of the storage function to query.
        :param params: Parameters for the query.
        :return: Query result.
        """
        try:
            result = self.substrate.query(
                module=self.pallet_name,
                storage_function=function_name,
                params=params or []
            )
            logger.debug(f"Query successful: {function_name} with params {params}")
            return result
        except Exception as e:
            logger.error(f"Query failed: {e}")
            raise ValueError(f"Query failed: {e}") from e
