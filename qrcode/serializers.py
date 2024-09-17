from rest_framework import serializers

from base.serializers import KeypairSerializer


class GenerateQRCodeSerializer(KeypairSerializer):
    amount = serializers.IntegerField(required=True)
    type = serializers.CharField(required=True)


class ProcessQRCodeSerializer(serializers.Serializer):
    account_id = serializers.CharField(required=True)
    amount = serializers.CharField(required=True)