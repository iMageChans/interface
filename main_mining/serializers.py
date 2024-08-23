from rest_framework import serializers
from main_mining import models


class BurningSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    account_id = serializers.CharField(required=False)
    amount = serializers.IntegerField(required=True)

    def validate_amount(self, value):
        if value < 100:
            raise serializers.ValidationError("Amount must be at least 100.")
        return value


class BurningWithdrawSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)


class TotalBurnedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TotalBurned
        fields = ['totals']


class GetTotalBurnedSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)


class GetBurnUserPortfolioSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    account_id = serializers.CharField(required=False)


class GetReturnPercentSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)