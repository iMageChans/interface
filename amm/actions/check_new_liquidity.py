from base.actions import BaseActionsRead
from amm.service.read import Read


class CheckNewLiquidity(BaseActionsRead):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.results = Read(self.keypair).check_new_liquidity(
            usdt_liquidity=validated_data['usdt_liquidity'],
            d9_liquidity=validated_data['d9_liquidity']
        )
