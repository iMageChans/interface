from base.actions import BaseActionsExec
from amm.service.exec import Exec
from amm.service.read import Read
from balances.tasks import update_or_create_d9_balance_celery
from usdt.tasks import update_or_create_usdt_balance_celery
from amm.tasks import update_or_created_token_market_information_celery
from utils import numbers
from utils.JSONExtractor import extractor
from record import models


class RemoveLiquidity(BaseActionsExec):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        # self.exec =  Exec(self.keypair)
        # self.results = self.exec.remove_liquidity()
        # d9_balance = update_or_create_d9_balance_celery.delay(self.account_id.mate_data_address())
        # usdt_balance = update_or_create_usdt_balance_celery.delay(self.account_id.mate_data_address(),
        #                                                           self.keypair.private_key.hex())
        # update_or_created_token_market_information_celery.delay()



    def serializers(self):
        read = Read(self.keypair).contract_get_payment_info('remove_liquidity')
        data = {
            "d9": 100 * (1 - 0.03) - numbers.format_d9(read['partialFee'])
        }
        return data
        # values = extractor.get_transfer_data(self.results)
        # values.update({"block_number": self.exec.get_block_numbers(self.results.block_hash)})
        # values.update({"form_address": self.account_id.mate_data_address()})
        # values.update({"to_address": "Dn" + self.results.contract_address})
        # values.update({"d9": numbers.format_d9(self.d9_amount)})
        # values.update({"usdt": numbers.format_d9(self.usdt_amount)})
        # values.update({"actions": "add_liquidity"})
        # models.Transaction.objects.create(**values)
        # return values

    def is_success(self):
        return True
        # return self.results.is_success
