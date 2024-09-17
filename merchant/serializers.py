from rest_framework import serializers

from base.serializers import KeypairSerializer


class GetMerchantExpirySerializer(KeypairSerializer):
    account_id = serializers.CharField(required=False)


class GetUserMerchantProfileSerializer(KeypairSerializer):
    account_id = serializers.CharField(required=False)


class SubscribeSerializer(KeypairSerializer):
    usdt_base_units = serializers.IntegerField(required=True)


class RedeemD9Serializer(KeypairSerializer):
    pass


class GivePointsD9Serializer(KeypairSerializer):
    consumer_id = serializers.CharField(required=True)
    amount = serializers.FloatField(required=True)


class GivePointsUSDTSerializer(KeypairSerializer):
    consumer_id = serializers.CharField(required=True)
    amount = serializers.FloatField(required=True)


class USDTPaymentSerializer(KeypairSerializer):
    merchant_id = serializers.CharField(required=True)
    amount = serializers.FloatField(required=True)


class D9PaymentSerializer(KeypairSerializer):
    merchant_id = serializers.CharField(required=True)
    amount = serializers.FloatField(required=True)
