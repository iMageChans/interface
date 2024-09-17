from rest_framework import serializers
from amm.models import *
from base.field import RoundedFloatField
from base.serializers import KeypairSerializer
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


class GetReservesSerializer(KeypairSerializer):
    pass


class GetLiquidityProviderSerializer(KeypairSerializer):
    account_id = serializers.CharField(required=True)


class CheckNewLiquiditySerializer(KeypairSerializer):
    usdt_liquidity = serializers.FloatField(required=True)
    d9_liquidity = serializers.FloatField(required=True)


class ComputeExchangeRateSerializer(KeypairSerializer):
    from_currency = serializers.CharField(required=True)
    to_currency = serializers.CharField(required=True)
    from_amount = serializers.FloatField(required=True)


class EstimateExchangeSerializer(KeypairSerializer):
    from_currency = serializers.CharField(required=True)
    to_currency = serializers.CharField(required=True)
    from_amount = serializers.FloatField(required=True)


class CheckUSDTBalanceSerializer(KeypairSerializer):
    account_id = serializers.CharField(required=True)
    amount = serializers.FloatField(required=True)


class AddLiquiditySerializer(KeypairSerializer):
    usdt_amount = serializers.FloatField(required=True)
    d9_amount = serializers.FloatField(required=True)


class RemoveLiquiditySerializer(KeypairSerializer):
    percent = serializers.FloatField(required=True)


class GetD9Serializer(KeypairSerializer):
    amount = serializers.FloatField(required=True)


class GetUSDTSerializer(KeypairSerializer):
    amount = serializers.FloatField(required=True)


class GetTotalLpTokensSerializer(KeypairSerializer):
    pass