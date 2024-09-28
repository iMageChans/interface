# merchant/serializers.py

from rest_framework import serializers

class BaseSerializer(serializers.Serializer):
    # 移除 KeypairSerializer，直接使用 BaseSerializer
    pass

class SubscribeSerializer(BaseSerializer):
    amount = serializers.IntegerField(required=True)

class RedeemD9Serializer(BaseSerializer):
    pass

class GivePointsD9Serializer(BaseSerializer):
    to_address = serializers.CharField(required=True)
    amount = serializers.FloatField(required=True)

class GivePointsUSDTSerializer(BaseSerializer):
    to_address = serializers.CharField(required=True)
    amount = serializers.FloatField(required=True)

class USDTPaymentSerializer(BaseSerializer):
    to_address = serializers.CharField(required=True)
    amount = serializers.FloatField(required=True)

class D9PaymentSerializer(BaseSerializer):
    to_address = serializers.CharField(required=True)
    amount = serializers.FloatField(required=True)
