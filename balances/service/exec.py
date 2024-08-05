from scalecodec.base import ScaleType

from base.d9_pallets import D9PalletsExec


class Exec(D9PalletsExec):
    def __init__(self):
        super().__init__('Balances')

    def transfer(self, recipient: str, amount: int):
        """
        transfer funds from one account to another
        Args:
             recipient (str): recipient account address
             amount (int): amount to transfer in base units
        Returns:
             dict: extrinsic result
        """
        result = self.compose_call('transfer', {
            'dest': recipient,
            'value': amount
        })

        return result
