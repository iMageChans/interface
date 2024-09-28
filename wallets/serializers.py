# wallets/serializers.py

from rest_framework import serializers
from utils.keystone import ValidAddress
from wallets.models import Wallet
from utils.token_rate_calculation import DecimalTruncation


class BaseSerializer(serializers.Serializer):
    to_address = serializers.CharField(required=True)

    def validate(self, data):
        to_address = data.get('to_address')
        data['to_address'] = ValidAddress(address=to_address).get_valid_address()
        return data


class RetrieveWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['address', 'd9', 'usdt', 'created_at', 'updated_at', 'last_login']
        read_only_fields = ['address', 'd9', 'usdt', 'created_at', 'updated_at', 'last_login']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['d9'] = DecimalTruncation(5).format(instance.d9)
        representation['usdt'] = DecimalTruncation(2).format(instance.usdt)
        return representation



class D9BalancesSerializer(BaseSerializer):
    pass

class USDTBalancesSerializer(BaseSerializer):
    pass
