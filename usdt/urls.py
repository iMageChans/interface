from django.urls import path
from usdt.views import *

urlpatterns = [
    path('get/balances/', GetBalancesView.as_view(), name='get-balances'),
    path('total/supply/', TotalSupplyView.as_view(), name='total-supply'),
    path('approve/', ApproveView.as_view(), name='approve'),
    path('allowance/decrease/', DecreaseAllowanceView.as_view(), name='decrease-allowance'),
    path('allowance/increase/', IncreaseAllowanceView.as_view(), name='increase-allowance'),
    path('transfer/', TransferView.as_view(), name='transfer'),
    path('transfer/from/', TransferFromView.as_view(), name='transfer-from'),
    path('allowance/node/reward/', NodeRewardAllowanceView.as_view(), name='node-reward-allowance'),
    path('allowance/burn/mining/', BurnMiningAllowanceView.as_view(), name='burn-mining-allowance'),
    path('allowance/main/mining/', MainMiningAllowanceView.as_view(), name='main-mining-allowance'),
    path('allowance/mining/', MiningAllowanceView.as_view(), name='mining-allowance'),
    path('allowance/market/maker/', MarketMakerAllowanceView.as_view(), name='market-maker-allowance'),
    path('allowance/usdt/', USDTAllowanceView.as_view(), name='usdt-allowance'),
    path('allowance/merchant/', MerchantAllowanceView.as_view(), name='merchant-allowance'),
    path('allowance/cross/chain/', CrossChainAllowanceView.as_view(), name='cross-chain-allowance'),
]