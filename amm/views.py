from base.views import BaseView
from amm import serializers
from amm import actions


class GetReservesView(BaseView):
    serializer_class = serializers.GetReservesSerializer
    action_class = actions.GetReserves


class GetLiquidityProviderView(BaseView):
    serializer_class = serializers.GetLiquidityProviderSerializer
    action_class = actions.GetLiquidityProvider


class CheckNewLiquidityView(BaseView):
    serializer_class = serializers.CheckNewLiquiditySerializer
    action_class = actions.CheckNewLiquidity


class ComputeExchangeRateView(BaseView):
    serializer_class = serializers.ComputeExchangeRateSerializer
    action_class = actions.ComputeExchangeRate


class EstimateExchangeView(BaseView):
    serializer_class = serializers.EstimateExchangeSerializer
    action_class = actions.EstimateExchange


class CheckUSDTBalanceView(BaseView):
    serializer_class = serializers.CheckUSDTBalanceSerializer
    action_class = actions.CheckUSDTBalance


class AddLiquidityView(BaseView):
    serializer_class = serializers.AddLiquiditySerializer
    action_class = actions.AddLiquidity


class RemoveLiquidityView(BaseView):
    serializer_class = serializers.RemoveLiquiditySerializer
    action_class = actions.RemoveLiquidity


class GetD9View(BaseView):
    serializer_class = serializers.GetD9Serializer
    action_class = actions.GetD9


class GetUSDTView(BaseView):
    serializer_class = serializers.GetUSDTSerializer
    action_class = actions.GetUSDT
