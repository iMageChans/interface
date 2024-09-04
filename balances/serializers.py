from rest_framework import serializers


class GetBalancesSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)
    account_id = serializers.CharField(required=False)


class TransferSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)
    to_address = serializers.CharField(required=True)
    amount = serializers.IntegerField(required=True)