from rest_framework import serializers
from amm.models import *
from base.field import RoundedFloatField
from utils.numbers import DecimalTruncation


class TokenMarketInformationSerializer(serializers.ModelSerializer):
    d9_token = serializers.SerializerMethodField()
    usdt_token = serializers.SerializerMethodField()
    d9_rate = RoundedFloatField(decimals=4)
    usdt_rate = RoundedFloatField(decimals=5)

    class Meta:
        model = TokenMarketInformation
        fields = ['d9_token', 'usdt_token', 'd9_rate', 'usdt_rate']

    def get_d9_token(self, obj):
        return DecimalTruncation(2).format_d9(obj.d9_token)

    def get_usdt_token(self, obj):
        return DecimalTruncation(2).format_usdt(obj.usdt_token)


class GetReservesSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)


class GetLiquidityProviderSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)
    account_id = serializers.CharField(required=True)


class CheckNewLiquiditySerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)
    usdt_liquidity = serializers.IntegerField(required=True)
    d9_liquidity = serializers.IntegerField(required=True)


class ComputeExchangeRateSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)
    from_currency = serializers.CharField(required=True)
    to_currency = serializers.CharField(required=True)
    from_amount = serializers.IntegerField(required=True)


class EstimateExchangeSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)
    from_currency = serializers.CharField(required=True)
    to_currency = serializers.CharField(required=True)
    from_amount = serializers.FloatField(required=True)


class CheckUSDTBalanceSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)
    account_id = serializers.CharField(required=True)
    amount = serializers.IntegerField(required=True)


class AddLiquiditySerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)
    usdt_amount = serializers.IntegerField(required=True)
    d9_amount = serializers.IntegerField(required=True)


class RemoveLiquiditySerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)
    percent = serializers.IntegerField(required=True)


class GetD9Serializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)
    amount = serializers.IntegerField(required=True)


class GetUSDTSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)
    amount = serializers.IntegerField(required=True)


class GetTotalLpTokensSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)