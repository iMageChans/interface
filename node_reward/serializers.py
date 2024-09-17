from rest_framework import serializers

from base.serializers import KeypairSerializer


class GetVoteLimitSerializer(KeypairSerializer):
    pass


class GetNodeRewardsDataSerializer(KeypairSerializer):
    node_id = serializers.CharField(required=True)


class WithdrawRewardSerializer(KeypairSerializer):
    node_id = serializers.CharField(required=True)