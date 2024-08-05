from base.actions import BaseActionsRead
from balances.tasks import update_or_create_d9_balance_celery
from users_profile.serializers import *


class GetBalances(BaseActionsRead):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        try:
            user_balances = UserBalances.objects.get(account_id=self.account_id.mate_data_address())
            self.results = UserBalancesSerializer(user_balances).data
        except UserBalances.DoesNotExist:
            self.results = update_or_create_d9_balance_celery(account_id=self.account_id.mate_data_address())

    def serializers(self):
        return self.results

    def is_success(self):
        return True
