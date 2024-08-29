from base.actions import BaseActionsRead
from users_profile.serializers import *
from merchant.tasks import update_or_created_get_merchant_expiry_celery
from merchant.service.read import Read
from utils.JSONExtractor import extractor


class GetMerchantExpiry(BaseActionsRead):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        merchant_read = Read(self.keypair)
        self.results = merchant_read.get_merchant_expiry(self.account_id.get_valid_address())

    def serializers(self):
        return extractor.get_data_or_err(self.results.value_serialized)

    def is_success(self):
        return True
