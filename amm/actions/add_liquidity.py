from base.actions import BaseActionsExec
from usdt.service.exec import Exec as USDTExec
from amm.service.exec import Exec
from amm.service.read import Read
from utils import numbers
from amm.tasks import update_or_created_token_market_information_celery
from balances.tasks import update_or_create_d9_balance_celery
from usdt.tasks import update_or_create_usdt_balance_celery
from utils.JSONExtractor import extractor
from record import models


class AddLiquidity(BaseActionsExec):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.usdt_amount = validated_data['usdt_amount']
        self.d9_amount = validated_data['d9_amount']
        self.exec = Exec(self.keypair)
        self.results = Exec(self.keypair).add_liquidity(
            usdt_amount=self.usdt_amount,
            d9_amount=self.d9_amount
        )



    def serializers(self):
        values = extractor.get_transfer_data(self.results)
        return values

    def is_success(self):
        if self.results.is_success:
            d9_balance = update_or_create_d9_balance_celery.delay(self.account_id.mate_data_address())
            usdt_balance = update_or_create_usdt_balance_celery.delay(self.account_id.mate_data_address(),
                                                                      self.keypair.private_key.hex())
            update_or_created_token_market_information_celery.delay()
        return self.results.is_success
