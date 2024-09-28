from substrateinterface import Keypair
from typing import Union, Optional
import logging

logger = logging.getLogger(__name__)


def check_keypair(keypair: Union[str, list], path: Optional[str] = None) -> Keypair:
    try:
        if path:
            uri = f"{keypair}{path}"
            return Keypair.create_from_uri(uri, ss58_format=9)

        if isinstance(keypair, list):
            mnemonic = ' '.join(keypair)
            return Keypair.create_from_mnemonic(mnemonic, ss58_format=9)

        if Keypair.validate_mnemonic(keypair):
            return Keypair.create_from_mnemonic(keypair, ss58_format=9)

        return Keypair.create_from_private_key(keypair, ss58_format=9)

    except Exception as e:
        logger.error(f"Invalid keypair: {e}")
        raise ValueError("Invalid keypair provided.") from e


class ValidAddress:
    PREFIX = "Dn"

    def __init__(self, address: str):
        self.address = address

    def get_valid_address(self) -> Optional[str]:
        if not self.address.startswith(self.PREFIX):
            logger.error("Invalid prefix.")
            return None

        actual_address = self.address[len(self.PREFIX):]
        try:
            Keypair(ss58_address=actual_address)
            return actual_address
        except ValueError as e:
            logger.error(f"Invalid address: {e}")
            return None

    def get_original_address(self) -> str:
        return self.address
