from base.actions import BaseActionsExec
from amm.service.exec import Exec
from amm.service.read import Read
from utils import numbers
from balances.tasks import update_or_create_d9_balance_celery
from usdt.tasks import update_or_create_usdt_balance_celery
from amm.tasks import update_or_created_token_market_information_celery
from utils.JSONExtractor import extractor
from record import models


class GetD9(BaseActionsExec):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.usdt = validated_data['amount']
        self.results = Exec(self.keypair).get_d9(
            usdt=numbers.to_usdt(self.usdt),
        )

        d9_balance = update_or_create_d9_balance_celery.delay(self.account_id.mate_data_address())
        usdt_balance = update_or_create_usdt_balance_celery.delay(self.account_id.mate_data_address(),
                                                                  self.keypair.private_key.hex())
        update_or_created_token_market_information_celery.delay()


    def serializers(self):
        read = Read(self.keypair)
        data = extractor.get_data_or_err(read.get_d9(usdt=numbers.to_usdt(self.usdt)).value_serialized)
        d9 = numbers.format_d9(data)
        values = extractor.get_transfer_data(self.results)
        values.update({"block_number": read.get_block_numbers(self.results.block_hash)})
        values.update({"form_address": self.account_id.mate_data_address()})
        values.update({"to_address": "Dn" + self.results.contract_address})
        values.update({"d9": d9})
        values.update({"usdt": self.usdt})
        values.update({"actions": "get_d9"})
        models.Transaction.objects.create(**values)
        return values