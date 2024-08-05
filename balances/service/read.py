from scalecodec.base import ScaleType

from base.d9_pallets import D9PalletsRead


class Read(D9PalletsRead):
    def __init__(self):
        super().__init__('Balances')

    def get_balances(self, account_id: str) -> ScaleType:
        """
        gets balance from chain
        Args:
             account_id (str): account address
        Returns:
             float: balance
        """
        return self.d9_interface.query('System', 'Account', [account_id])
