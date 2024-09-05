from rest_framework import serializers


class GetMerchantExpirySerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)
    account_id = serializers.CharField(required=False)


class GetUserMerchantProfileSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)
    account_id = serializers.CharField(required=False)


class SubscribeSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)
    usdt_base_units = serializers.IntegerField(required=True)


class RedeemD9Serializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)


class GivePointsD9Serializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)
    consumer_id = serializers.CharField(required=True)
    amount = serializers.IntegerField(required=True)


class GivePointsUSDTSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)
    consumer_id = serializers.CharField(required=True)
    amount = serializers.IntegerField(required=True)


class USDTPaymentSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)
    merchant_id = serializers.CharField(required=True)
    amount = serializers.FloatField(required=True)


class D9PaymentSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)
    merchant_id = serializers.CharField(required=True)
    amount = serializers.FloatField(required=True)
