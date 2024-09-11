from rest_framework import serializers
from usdt.models import CurrencyProfile


class GetBalancesSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)
    account_id = serializers.CharField(required=False)


class TotalSupplySerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)


class ApproveSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)
    account_id = serializers.CharField(required=True)
    amount = serializers.IntegerField(required=True)


class DecreaseAllowanceSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)
    account_id = serializers.CharField(required=True)
    amount = serializers.IntegerField(required=True)


class IncreaseAllowanceSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)
    to_address = serializers.CharField(required=True)
    amount = serializers.FloatField(required=True)


class NodeRewardAllowanceSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)
    amount = serializers.IntegerField(required=True)


class BurnMiningAllowanceSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)
    amount = serializers.IntegerField(required=True)


class MainMiningAllowanceSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)
    amount = serializers.IntegerField(required=True)


class MiningAllowanceSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)
    amount = serializers.IntegerField(required=True)


class MarketMakerAllowanceSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)
    amount = serializers.IntegerField(required=True)


class USDTAllowanceSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)
    amount = serializers.IntegerField(required=True)


class MerchantAllowanceSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)
    amount = serializers.IntegerField(required=True)


class CrossChainAllowanceSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)
    amount = serializers.IntegerField(required=True)


class TransferSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)
    to_address = serializers.CharField(required=True)
    amount = serializers.IntegerField(required=True)


class TransferFromSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)
    from_address = serializers.CharField(required=True)
    to_address = serializers.CharField(required=True)
    amount = serializers.IntegerField(required=True)


class GetCurrencyProfileSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)


class CurrencyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyProfile
        fields = '__all__'


class GetAllowanceSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)
    from_address = serializers.CharField(required=True)
    to_address = serializers.CharField(required=True)
