from base.views import BaseView
from balances import serializers
from balances import actions


class GetBalancesView(BaseView):
    serializer_class = serializers.GetBalancesSerializer
    action_class = actions.GetBalances


class TransfersView(BaseView):
    serializer_class = serializers.TransferSerializer
    action_class = actions.Transfer
