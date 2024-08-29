from django.urls import path
from amm.views import *

urlpatterns = [
    path('get/reserves/', GetReservesView.as_view(), name='get-reserves'),
    path('get/liquidity/provider/', GetLiquidityProviderView.as_view(), name='get-liquidity-provider'),
    path('check/new/liquidity/', CheckNewLiquidityView.as_view(), name='check-new-liquidity'),
    path('compute/exchange/rate/', ComputeExchangeRateView.as_view(), name='compute-exchange-rate'),
    path('estimate/exchange/', EstimateExchangeView.as_view(), name='compute-exchange-rate'),
    path('check/usdt/balance/', CheckUSDTBalanceView.as_view(), name='check-usdt-balance'),
    path('add/liquidity/', AddLiquidityView.as_view(), name='add-liquidity'),
    path('remove/liquidity/', RemoveLiquidityView.as_view(), name='remove-liquidity'),
    path('get/d9/', GetD9View.as_view(), name='get-d9'),
    path('get/usdt/', GetUSDTView.as_view(), name='get-usdt'),
    path('get/total/lp/tokens/', GetTotalLpTokensView.as_view(), name='get-total-lp-tokens'),
]