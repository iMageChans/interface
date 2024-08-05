from django.urls import path
from node_reward.views import *

urlpatterns = [
    path('get/vote/limit/', GetVoteLimitView.as_view(), name='get-vote-limit'),
    path('get/node/rewards/data/', GetNodeRewardsDataView.as_view(), name='get-node-rewards-data'),
    path('withdraw/reward/', WithdrawRewardView.as_view(), name='withdraw-reward'),
]