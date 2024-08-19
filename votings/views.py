from base.views import BaseView
from votings import serializers
from votings import actions


class GetNumberOfCandidatesView(BaseView):
    serializer_class = serializers.GetNumberOfCandidatesSerializer
    action_class = actions.GetNumberOfCandidates


class CurrentSessionIndexView(BaseView):
    serializer_class = serializers.CurrentSessionIndexSerializer
    action_class = actions.CurrentSessionIndex


class ValidatorStatsView(BaseView):
    serializer_class = serializers.ValidatorStatsSerializer
    action_class = actions.ValidatorStats


class GetNodeAccumulativeVotesView(BaseView):
    serializer_class = serializers.GetNodeAccumulativeVotesSerializer
    action_class = actions.GetNodeAccumulativeVotes


class GetNodeMetaDataView(BaseView):
    serializer_class = serializers.GetNodeMetaDataSerializer
    action_class = actions.GetNodeMetaData


class NodeToUserVoteTotalsView(BaseView):
    serializer_class = serializers.NodeToUserVoteTotalsSerializer
    action_class = actions.NodeToUserVoteTotals


class GetSessionNodeListView(BaseView):
    serializer_class = serializers.GetSessionNodeListSerializer
    action_class = actions.GetSessionNodeList


class AddVotingInterestView(BaseView):
    serializer_class = serializers.AddVotingInterestSerializer
    action_class = actions.AddVotingInterest


class ChangeCandidateNameView(BaseView):
    serializer_class = serializers.ChangeCandidateNameSerializer
    action_class = actions.ChangeCandidateName


class ChangeCandidateSupportShareView(BaseView):
    serializer_class = serializers.ChangeCandidateSupportShareSerializer
    action_class = actions.ChangeCandidateSupportShare


class DelegateVotesView(BaseView):
    serializer_class = serializers.DelegateVotesSerializer
    action_class = actions.DelegateVotes


class GetRankView(BaseView):
    serializer_class = serializers.GetRankSerializer
    action_class = actions.GetRank


class TryRemoveVotesFromCandidateView(BaseView):
    serializer_class = serializers.TryRemoveVotesFromCandidateSerializer
    action_class = actions.TryRemoveVotesFromCandidate


class UsersVotingInterestsView(BaseView):
    serializer_class = serializers.UsersVotingInterestsSerializer
    action_class = actions.UsersVotingInterests
