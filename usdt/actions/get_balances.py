from base.actions import BaseActionsRead
from usdt.service.read import Read
from usdt.tasks import update_or_create_usdt_balance_celery
from users_profile.serializers import *
from utils import numbers
from utils.JSONExtractor import extractor


class GetBalances(BaseActionsRead):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        usdt_read = Read(self.keypair)
        self.results = usdt_read.balance_of(owner=self.account_id.get_valid_address())

    def serializers(self):
        return {"balance_usdt": numbers
                    .DecimalTruncation(2)
                    .format_usdt(extractor.get_data_or_err(self.results.value_serialized))}

    def is_success(self):
        return True
