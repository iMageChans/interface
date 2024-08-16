from django.urls import path
from votings.views import *

urlpatterns = [
    path('get/number/candidates/', GetNumberOfCandidatesView.as_view(), name='get-number-candidates'),
    path('current/session/index/', CurrentSessionIndexView.as_view(), name='current-session-index'),
    path('validator/stats/', ValidatorStatsView.as_view(), name='validator-stats'),
    path('get/node/accumulative/votes/', GetNodeAccumulativeVotesView.as_view(), name='get-node-accumulative-votes'),
    path('get/node/metadata/', GetNodeMetaDataView.as_view(), name='get-node-metadata'),
    path('node/user/vote/totals/', NodeToUserVoteTotalsView.as_view(), name='node-user-vote-totals'),
    path('get/session/node/list/', GetSessionNodeListView.as_view(), name='get-session-node-list'),
    path('add/voting/interest/', AddVotingInterestView.as_view(), name='add-voting-interest'),
    path('change/candidate/name/', ChangeCandidateNameView.as_view(), name='change-candidate-name'),
    path('change/candidate/support/share/', ChangeCandidateSupportShareView.as_view(), name='change-candidate-support-share'),
    path('delegate/votes/', DelegateVotesView.as_view(), name='delegate-votes'),
    path('get/rank/', GetRankView.as_view(), name='get-rank'),
    path('try/remove/votes/from/candidate/', TryRemoveVotesFromCandidateView.as_view(), name='try-remove-votes-from-candidate'),
]
