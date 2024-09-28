from base.actions import BaseActionsExec
from amm.service.exec import Exec
from utils import numbers
from balances.tasks import update_or_create_d9_balance_celery
from usdt.tasks import update_or_create_usdt_balance_celery
from amm.tasks import update_or_created_token_market_information_celery
from utils.JSONExtractor import JSONExtractor


class GetD9(BaseActionsExec):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.usdt = validated_data['amount']
        self.results = Exec(self.keypair).get_d9(
            usdt=numbers.to_usdt(self.usdt),
        )


    def serializers(self):
        return JSONExtractor().get_data_or_err(self.results)

    def is_success(self):
        if self.results.is_success:
            d9_balance = update_or_create_d9_balance_celery.delay(self.account_id.mate_data_address())
            usdt_balance = update_or_create_usdt_balance_celery.delay(self.account_id.mate_data_address(),
                                                                      self.keypair.private_key.hex())
            update_or_created_token_market_information_celery.delay()
        return self.results.is_success