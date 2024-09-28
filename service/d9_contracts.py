# base/d9_contracts.py

from substrateinterface.contracts import ContractInstance
from substrateinterface import Keypair, SubstrateInterface
import logging
from typing import Optional

logger = logging.getLogger(__name__)

class D9Contract:
    def __init__(self, contract_address: str, metadata_file: str, keypair: Keypair, substrate: SubstrateInterface):
        self.keypair = keypair
        self.substrate = substrate
        try:
            self.contract = ContractInstance.create_from_address(
                contract_address=contract_address,
                metadata_file=metadata_file,
                substrate=self.substrate,
            )
            logger.info(f"Contract instance created for address: {contract_address}")
        except Exception as e:
            logger.error(f"Failed to create contract instance: {e}")
            raise ValueError(f"Failed to create contract instance: {e}") from e

    def contract_exec(self, call_name: str, call_params: Optional[dict] = None, value: int = 0):
        """
        Execute a contract function that alters the contract state.
        """
        try:
            result = self.contract.exec(self.keypair, call_name, call_params or {}, value)
            logger.info(f"Contract exec successful: {call_name} with params {call_params}")
            return result
        except Exception as e:
            logger.error(f"Contract exec failed: {e}")
            raise ValueError(f"Contract exec failed: {e}") from e

    def contract_read(self, call_name: str, call_params: Optional[dict] = None, value: int = 0):
        """
        Read data from the contract without altering its state.
        """
        try:
            result = self.contract.read(self.keypair, call_name, call_params or {}, value)
            logger.info(f"Contract read successful: {call_name} with params {call_params}")
            return result
        except Exception as e:
            logger.error(f"Contract read failed: {e}")
            raise ValueError(f"Contract read failed: {e}") from e
