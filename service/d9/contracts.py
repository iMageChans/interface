from base.network import D9Pallets


class D9PalletsBalances(D9Pallets):
    def __init__(self):
        super().__init__('Balances')

    def get_balances(self, to_address: str):
        """
        Get the balance of the given account.

        Parameters:
            to_address (str): The address of the account.

        Returns:
            float: The balance of the account.
        """
        return self.substrate.query('free_balance', {'account': to_address})

    def d9_transfer(self, to_address: str, amount: int):
        """
        Transfer funds from one account to another.

        Parameters:
            to_address (str): The address of the recipient account.
            amount (int): The amount to transfer in base units.

        Returns:
            dict: The extrinsic result.
        """
        return self.compose_call('transfer', {'dest': to_address, 'value': amount})