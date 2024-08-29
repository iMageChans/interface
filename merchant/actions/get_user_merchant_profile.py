from base.actions import BaseActionsRead
from merchant.service.read import Read
from utils.JSONExtractor import extractor


class GetUserMerchantProfile(BaseActionsRead):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        merchant_read = Read(self.keypair)
        self.results = merchant_read.get_user_merchant_profile(self.account_id.get_valid_address())

    def serializers(self):
        return extractor.get_merchant_portfolio(self.results.value_serialized)

    def is_success(self):
        return True
