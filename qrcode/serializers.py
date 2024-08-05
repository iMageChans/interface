from rest_framework import serializers


class GenerateQRCodeSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    amount = serializers.IntegerField(required=True)


class ProcessQRCodeSerializer(serializers.Serializer):
    account_id = serializers.CharField(required=True)
    amount = serializers.CharField(required=True)