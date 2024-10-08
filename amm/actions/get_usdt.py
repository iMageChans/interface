from base.actions import BaseActionsExec
from amm.service.exec import Exec
from amm.service.read import Read
from utils import numbers
from balances.tasks import update_or_create_d9_balance_celery
from usdt.tasks import update_or_create_usdt_balance_celery
from amm.tasks import update_or_created_token_market_information_celery
from utils.JSONExtractor import extractor
from record import models


class GetUSDT(BaseActionsExec):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.d9 = validated_data['amount']
        self.exec = Exec(self.keypair)
        self.results = self.exec.get_usdt(
            d9_amount=numbers.to_d9(self.d9),
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