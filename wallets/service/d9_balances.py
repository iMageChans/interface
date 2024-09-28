from base.network import D9Pallets


class D9Balances(D9Pallets):
    def __init__(self):
        super().__init__(pallet_name='Balances')

    def d9_balances(self, to_address: str):
        """
        gets balance from chain
        Args:
             account_id (str): account address
        Returns:
             float: balance
             :param address:
        """
        return self.substrate.query('System', 'Account', [to_address])