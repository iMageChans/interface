from base.views import BaseView
from usdt import serializers
from usdt import actions


class GetBalancesView(BaseView):
    serializer_class = serializers.GetBalancesSerializer
    action_class = actions.GetBalances


class TotalSupplyView(BaseView):
    serializer_class = serializers.TotalSupplySerializer
    action_class = actions.TotalSupply


class ApproveView(BaseView):
    serializer_class = serializers.ApproveSerializer
    action_class = actions.Approve


class DecreaseAllowanceView(BaseView):
    serializer_class = serializers.DecreaseAllowanceSerializer
    action_class = actions.DecreaseAllowance


class IncreaseAllowanceView(BaseView):
    serializer_class = serializers.IncreaseAllowanceSerializer
    action_class = actions.IncreaseAllowance


class TransferView(BaseView):
    serializer_class = serializers.TransferSerializer
    action_class = actions.Transfer


class TransferFromView(BaseView):
    serializer_class = serializers.TransferFromSerializer
    action_class = actions.TransferFrom


class NodeRewardAllowanceView(BaseView):
    serializer_class = serializers.NodeRewardAllowanceSerializer
    action_class = actions.NodeRewardAllowance


class BurnMiningAllowanceView(BaseView):
    serializer_class = serializers.BurnMiningAllowanceSerializer
    action_class = actions.BurnMiningAllowance


class MainMiningAllowanceView(BaseView):
    serializer_class = serializers.MainMiningAllowanceSerializer
    action_class = actions.MainMiningAllowance


class MiningAllowanceView(BaseView):
    serializer_class = serializers.MiningAllowanceSerializer
    action_class = actions.MiningAllowance


class MarketMakerAllowanceView(BaseView):
    serializer_class = serializers.MarketMakerAllowanceSerializer
    action_class = actions.MarketMakerAllowance


class USDTAllowanceView(BaseView):
    serializer_class = serializers.USDTAllowanceSerializer
    action_class = actions.USDTAllowance


class MerchantAllowanceView(BaseView):
    serializer_class = serializers.MerchantAllowanceSerializer
    action_class = actions.MerchantAllowance


class CrossChainAllowanceView(BaseView):
    serializer_class = serializers.CrossChainAllowanceSerializer
    action_class = actions.CrossChainAllowance


class PriceRateView(BaseView):
    serializer_class = serializers.GetCurrencyProfileSerializer
    action_class = actions.PriceRate

class GetAllowanceView(BaseView):
    serializer_class = serializers.ApproveSerializer
    action_class = actions.GetAllowance