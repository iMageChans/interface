from rest_framework import serializers


class GenerateQRCodeSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)
    amount = serializers.IntegerField(required=True)
    type = serializers.CharField(required=True)


class ProcessQRCodeSerializer(serializers.Serializer):
    account_id = serializers.CharField(required=True)
    amount = serializers.CharField(required=True)