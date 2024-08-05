from base.actions import BaseActionsExec
from amm.service.exec import Exec
from balances.tasks import update_or_create_d9_balance_celery
from usdt.tasks import update_or_create_usdt_balance_celery
from amm.tasks import update_or_created_token_market_information_celery


class RemoveLiquidity(BaseActionsExec):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.results = Exec(self.keypair).remove_liquidity()
        d9_balance = update_or_create_d9_balance_celery.delay(self.account_id.mate_data_address())
        usdt_balance = update_or_create_usdt_balance_celery.delay(self.account_id.mate_data_address(),
                                                                  self.keypair.private_key.hex())
        update_or_created_token_market_information_celery.delay()
