from base.views import BaseView
from main_mining import serializers
from main_mining import actions


class GetTotalBurnedView(BaseView):
    serializer_class = serializers.GetTotalBurnedSerializer
    action_class = actions.GetTotalBurned


class GetUserBurningProfileView(BaseView):
    serializer_class = serializers.GetBurnUserPortfolioSerializer
    action_class = actions.GetUserBurningProfile


class BurningView(BaseView):
    serializer_class = serializers.BurningSerializer
    action_class = actions.Burning


class WithdrawView(BaseView):
    serializer_class = serializers.BurningWithdrawSerializer
    action_class = actions.Withdraw
