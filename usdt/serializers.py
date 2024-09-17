from rest_framework import serializers

from base.serializers import KeypairSerializer
from usdt.models import CurrencyProfile


class GetBalancesSerializer(KeypairSerializer):
    account_id = serializers.CharField(required=False)


class TotalSupplySerializer(KeypairSerializer):
    pass


class ApproveSerializer(KeypairSerializer):
    to_address = serializers.CharField(required=True)
    amount = serializers.FloatField(required=True)


class DecreaseAllowanceSerializer(KeypairSerializer):
    to_address = serializers.CharField(required=True)
    amount = serializers.FloatField(required=True)


class IncreaseAllowanceSerializer(KeypairSerializer):
    to_address = serializers.CharField(required=True)
    amount = serializers.FloatField(required=True)


class NodeRewardAllowanceSerializer(KeypairSerializer):
    amount = serializers.FloatField(required=True)


class BurnMiningAllowanceSerializer(KeypairSerializer):
    amount = serializers.FloatField(required=True)


class MainMiningAllowanceSerializer(KeypairSerializer):
    amount = serializers.FloatField(required=True)


class MiningAllowanceSerializer(KeypairSerializer):
    amount = serializers.FloatField(required=True)


class MarketMakerAllowanceSerializer(KeypairSerializer):
    amount = serializers.FloatField(required=True)


class USDTAllowanceSerializer(KeypairSerializer):
    amount = serializers.FloatField(required=True)


class MerchantAllowanceSerializer(KeypairSerializer):
    amount = serializers.FloatField(required=True)


class CrossChainAllowanceSerializer(KeypairSerializer):
    amount = serializers.FloatField(required=True)


class TransferSerializer(KeypairSerializer):
    to_address = serializers.CharField(required=True)
    amount = serializers.FloatField(required=True)


class TransferFromSerializer(KeypairSerializer):
    from_address = serializers.CharField(required=True)
    to_address = serializers.CharField(required=True)
    amount = serializers.FloatField(required=True)


class GetCurrencyProfileSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)


class CurrencyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyProfile
        fields = '__all__'


class GetAllowanceSerializer(KeypairSerializer):
    from_address = serializers.CharField(required=True)
    to_address = serializers.CharField(required=True)
