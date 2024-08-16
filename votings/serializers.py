from rest_framework import serializers
from votings.models import Rank


class GetNumberOfCandidatesSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)


class CurrentSessionIndexSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)


class ValidatorStatsSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    validator_id = serializers.CharField(required=True)


class GetNodeAccumulativeVotesSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    node_id = serializers.CharField(required=True)


class GetNodeMetaDataSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    node_id = serializers.CharField(required=True)


class NodeToUserVoteTotalsSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    node_id = serializers.CharField(required=False)
    user_id = serializers.CharField(required=False)


class GetSessionNodeListSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    session_index = serializers.IntegerField(required=True)


class AddVotingInterestSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    account_id = serializers.CharField(required=True)
    amount_to_burn = serializers.IntegerField(required=True)


class ChangeCandidateNameSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    name = serializers.CharField(required=True)


class ChangeCandidateSupportShareSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    percent = serializers.IntegerField(required=True)


class DelegateVotesSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    candidate = serializers.CharField(required=True)
    amount = serializers.IntegerField(required=True)


class GetRankSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)


class RankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rank
        exclude = ['id']

