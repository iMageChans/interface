from base.actions import BaseActionsRead
from main_mining import tasks
from users_profile.serializers import *


class GetUserBurningProfile(BaseActionsRead):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        try:
            user_burning_profile = UserBurningProfile.objects.get(pk=self.account_id.mate_data_address())
            self.results = UserBurningProfileSerializer(user_burning_profile).data
        except UserBurningProfile.DoesNotExist:
            user_burning_profile = tasks.update_or_create_user_burning_profile_celery(
                account_id=self.account_id.mate_data_address(),
                keypair=self.keypair.private_key.hex()
            )
            self.results = UserBurningProfileSerializer(user_burning_profile).data

    def serializers(self):
        return self.results

    def is_success(self):
        return True