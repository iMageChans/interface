from base.actions import BaseActionsRead
from users_profile.serializers import *
from merchant.tasks import update_or_created_get_merchant_expiry_celery


class GetMerchantExpiry(BaseActionsRead):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        try:
            merchant_expiry = MerchantExpiry.objects.get(pk=self.account_id.mate_data_address())
            self.results = MerchantExpirySerializer(merchant_expiry).data
        except MerchantExpiry.DoesNotExist:
            merchant_expiry = update_or_created_get_merchant_expiry_celery(
                account_id=self.account_id.mate_data_address(),
                keypair=self.keypair.private_key.hex()
            )
            self.results = MerchantExpirySerializer(merchant_expiry).data

    def serializers(self):
        return self.results

    def is_success(self):
        return True
