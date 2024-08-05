from base.actions import BaseActionsRead
from users_profile.serializers import *
from merchant.tasks import update_or_created_get_user_merchant_profile_celery


class GetUserMerchantProfile(BaseActionsRead):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        try:
            user_merchant_profile = UserMerchantProfile.objects.get(pk=self.account_id.mate_data_address())
            self.results = UserMerchantProfileSerializer(user_merchant_profile).data
        except UserMerchantProfile.DoesNotExist:
            user_merchant_profile = update_or_created_get_user_merchant_profile_celery(
                account_id=self.account_id.mate_data_address(),
                keypair=self.keypair.private_key.hex()
            )
            self.results = MerchantExpirySerializer(user_merchant_profile).data

    def serializers(self):
        return self.results

    def is_success(self):
        return True
