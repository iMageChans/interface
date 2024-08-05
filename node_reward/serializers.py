from rest_framework import serializers


class GetVoteLimitSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)


class GetNodeRewardsDataSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    node_id = serializers.CharField(required=True)


class WithdrawRewardSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    node_id = serializers.CharField(required=True)