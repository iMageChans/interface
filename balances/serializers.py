from rest_framework import serializers

from base.serializers import KeypairSerializer


class GetBalancesSerializer(KeypairSerializer):
    account_id = serializers.CharField(required=False)


class TransferSerializer(KeypairSerializer):
    to_address = serializers.CharField(required=True)
    amount = serializers.FloatField(required=True)