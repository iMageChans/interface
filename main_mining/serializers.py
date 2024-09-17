from rest_framework import serializers

from base.serializers import KeypairSerializer
from main_mining import models


class BurningSerializer(KeypairSerializer):
    account_id = serializers.CharField(required=False)
    amount = serializers.IntegerField(required=True)

    def validate_amount(self, value):
        if value < 100:
            raise serializers.ValidationError("Amount must be at least 100.")
        return value


class BurningWithdrawSerializer(KeypairSerializer):
    pass


class TotalBurnedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TotalBurned
        fields = ['totals']


class GetTotalBurnedSerializer(KeypairSerializer):
    pass


class GetBurnUserPortfolioSerializer(KeypairSerializer):
    account_id = serializers.CharField(required=False)


class GetReturnPercentSerializer(KeypairSerializer):
    pass