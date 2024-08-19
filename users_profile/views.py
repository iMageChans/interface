from base.views import BaseView
from users_profile import serializers
from users_profile.actions.get_users_profile import GetUsersProfile
from users_profile.actions.get_user_to_node_vote import GetUserToNodeVote
from rest_framework import mixins


class GetUsersProfileView(BaseView):
    serializer_class = serializers.UsersProfileSerializer
    action_class = GetUsersProfile


class GetUserToNodeVoteView(BaseView):
    serializer_class = serializers.GetUserToNodeVoteSerializer
    action_class = GetUserToNodeVote



class TestView(mixins.ListModelMixin):
    pass