from base.actions import BaseActionsExec
from amm.service.exec import Exec
from utils import numbers
from amm.tasks import update_or_created_token_market_information_celery
from balances.tasks import update_or_create_d9_balance_celery
from usdt.tasks import update_or_create_usdt_balance_celery


class AddLiquidity(BaseActionsExec):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.usdt_amount = validated_data['usdt_amount']
        self.d9_amount = validated_data['d9_amount']
        self.results = Exec(self.keypair).add_liquidity(
            usdt_amount=numbers.to_d9(self.usdt_amount),
            d9_amount=numbers.to_usdt(self.d9_amount)
        )
        d9_balance = update_or_create_d9_balance_celery.delay(self.account_id.mate_data_address())
        usdt_balance = update_or_create_usdt_balance_celery.delay(self.account_id.mate_data_address(),
                                                                  self.keypair.private_key.hex())
        update_or_created_token_market_information_celery.delay()
