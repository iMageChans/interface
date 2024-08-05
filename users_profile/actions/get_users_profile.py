from base.actions import BaseActionsRead
from users_profile.celery.update_or_created_d9_balance import *
from users_profile.celery.update_or_create_usdt_balance import *
from users_profile.celery.update_or_create_user_burning_profile import *
from merchant.celery.update_or_created_get_merchant_expiry import *
from merchant.celery.update_or_created_get_user_merchant_profile import *


class GetUsersProfile(BaseActionsRead):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        d9_balance = update_or_create_d9_balance(self.account_id.mate_data_address())
        usdt_balance = update_or_create_usdt_balance(self.account_id.mate_data_address(),
                                                     self.keypair.private_key.hex())
        burning_profile = update_or_create_burning_profile(self.account_id.mate_data_address(),
                                                           self.keypair.private_key.hex())
        merchant_expiry = update_or_created_get_merchant_expiry(self.account_id.mate_data_address(),
                                                                self.keypair.private_key.hex())
        user_merchant_profile = update_or_created_get_user_merchant_profile(self.account_id.mate_data_address(),
                                                                            self.keypair.private_key.hex())
        self.results = dict()
        self.results.update({"account_id": self.account_id.mate_data_address()})
        self.results.update(d9_balance)
        self.results.update(usdt_balance)
        self.results.update({"burning_profile": UserBurningProfileSerializer(burning_profile).data})
        self.results.update(MerchantExpirySerializer(merchant_expiry).data)
        self.results.update({"merchant_profile": UserMerchantProfileSerializer(user_merchant_profile).data})

    def serializers(self):
        return self.results

    def is_success(self):
        if self.results:
            return True
        return False
