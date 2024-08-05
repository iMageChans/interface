from django.urls import path
from users_profile.views import *

urlpatterns = [
    path('get/', GetUsersProfileView.as_view(), name='get-users-profile'),
    path('get/user/node/vote/', GetUserToNodeVoteView.as_view(), name='get-user-node-vote'),
]
