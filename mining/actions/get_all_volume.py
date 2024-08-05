from base.actions import BaseActionsRead
from users_profile import models
from users_profile import serializers


class GetAllVolume(BaseActionsRead):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.main_mining_balance = models.UserBalances.objects.get(pk="DnwRGYShktZsxtKwXCCzqtLW7P1a5K2qDsaXEcRWxVYKGwH7d")
        self.mining_balance = models.UserBalances.objects.get(pk="DnzXB3VPHrnb9pzfJweLstBfmn5Xq3dEAFAbKKxTsQZg1entq")

    def serializers(self):
        main = serializers.UserBalancesSerializer(self.main_mining_balance).data
        mining = serializers.UserBalancesSerializer(self.mining_balance).data
        data = float(main['balance_d9']) + float(mining['balance_d9'])
        return data

    def is_success(self):
        return True
