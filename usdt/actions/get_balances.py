from base.actions import BaseActionsRead
from usdt.tasks import update_or_create_usdt_balance_celery
from users_profile.serializers import *


class GetBalances(BaseActionsRead):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        try:
            usdt_balances = USDTBalances.objects.get(pk=self.account_id.mate_data_address())
            self.results = USDTBalancesSerializer(usdt_balances).data
        except USDTBalances.DoesNotExist:
            self.results = update_or_create_usdt_balance_celery(
                account_id=self.account_id.mate_data_address(),
                keypair=self.keypair.private_key.hex()
            )

    def serializers(self):
        return self.results

    def is_success(self):
        return True
