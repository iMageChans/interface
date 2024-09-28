from usdt.abi.files import get_abi_files
from base.network import D9Contract
from substrateinterface import Keypair
from base.config import USDT_CONTRACT


class USDTBalances(D9Contract):

    def __init__(self, keypair: Keypair):
        super().__init__(
            contract_address=USDT_CONTRACT,
            metadata_file=get_abi_files(),
            keypair=keypair
        )

    def usdt_balances(self, to_address: str) -> float:
        """
        Retrieves the USDT token balance for a given address from the contract.

        Args:
            to_address (str): The wallet address to query.

        Returns:
            float: The USDT token balance.
        """
        params = {
            "owner": to_address,
        }

        return self.contract_read(call_name='PSP22::balance_of', call_params=params)