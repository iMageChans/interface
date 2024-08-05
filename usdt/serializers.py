from rest_framework import serializers


class GetBalancesSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    account_id = serializers.CharField(required=False)


class TotalSupplySerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)


class ApproveSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    account_id = serializers.CharField(required=True)
    amount = serializers.IntegerField(required=True)


class DecreaseAllowanceSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    account_id = serializers.CharField(required=True)
    amount = serializers.IntegerField(required=True)


class IncreaseAllowanceSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    account_id = serializers.CharField(required=True)
    amount = serializers.IntegerField(required=True)


class NodeRewardAllowanceSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    amount = serializers.IntegerField(required=True)


class BurnMiningAllowanceSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    amount = serializers.IntegerField(required=True)


class MainMiningAllowanceSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    amount = serializers.IntegerField(required=True)


class MiningAllowanceSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    amount = serializers.IntegerField(required=True)


class MarketMakerAllowanceSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    amount = serializers.IntegerField(required=True)


class USDTAllowanceSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    amount = serializers.IntegerField(required=True)


class MerchantAllowanceSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    amount = serializers.IntegerField(required=True)


class CrossChainAllowanceSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    amount = serializers.IntegerField(required=True)


class TransferSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    to_address = serializers.CharField(required=True)
    amount = serializers.IntegerField(required=True)


class TransferFromSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    from_address = serializers.CharField(required=True)
    to_address = serializers.CharField(required=True)
    amount = serializers.IntegerField(required=True)