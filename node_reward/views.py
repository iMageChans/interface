from base.views import BaseView
from node_reward import serializers
from node_reward import actions


class GetVoteLimitView(BaseView):
    serializer_class = serializers.GetVoteLimitSerializer
    action_class = actions.GetVoteLimit


class GetNodeRewardsDataView(BaseView):
    serializer_class = serializers.GetNodeRewardsDataSerializer
    action_class = actions.GetNodeRewardsData


class WithdrawRewardView(BaseView):
    serializer_class = serializers.WithdrawRewardSerializer
    action_class = actions.WithdrawReward
