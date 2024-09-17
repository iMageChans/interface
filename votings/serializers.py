from rest_framework import serializers

from base.serializers import KeypairSerializer
from votings.models import Rank


class GetNumberOfCandidatesSerializer(KeypairSerializer):
    pass


class CurrentSessionIndexSerializer(KeypairSerializer):
    pass


class ValidatorStatsSerializer(KeypairSerializer):
    validator_id = serializers.CharField(required=True)


class GetNodeAccumulativeVotesSerializer(KeypairSerializer):
    node_id = serializers.CharField(required=True)


class GetNodeMetaDataSerializer(KeypairSerializer):
    node_id = serializers.CharField(required=True)


class NodeToUserVoteTotalsSerializer(KeypairSerializer):
    node_id = serializers.CharField(required=True)
    user_id = serializers.CharField(required=False)


class GetSessionNodeListSerializer(KeypairSerializer):
    session_index = serializers.IntegerField(required=True)


class AddVotingInterestSerializer(KeypairSerializer):
    account_id = serializers.CharField(required=True)
    amount_to_burn = serializers.FloatField(required=True)


class ChangeCandidateNameSerializer(KeypairSerializer):
    name = serializers.CharField(required=True)


class ChangeCandidateSupportShareSerializer(KeypairSerializer):
    percent = serializers.IntegerField(required=True)


class TryRemoveVotesFromCandidateSerializer(KeypairSerializer):
    node_id = serializers.CharField(required=True)
    votes = serializers.IntegerField(required=True)


class DelegateVotesSerializer(KeypairSerializer):
    candidate = serializers.CharField(required=True)
    amount = serializers.FloatField(required=True)


class GetRankSerializer(KeypairSerializer):
    pass


class RankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rank
        exclude = ['id']


class UsersVotingInterestsSerializer(KeypairSerializer):
    pass

