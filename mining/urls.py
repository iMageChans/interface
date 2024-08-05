from django.urls import path
from mining.views import *

urlpatterns = [
    path('get/accumulative/reward/pool/', GetAccumulativeRewardPoolView.as_view(), name='get-accumulative-reward-pool'),
    path('get/merchant/volume/', GetMerchantVolumeView.as_view(), name='get-merchant-volume'),
    path('get/session/volume/', GetSessionVolumeView.as_view(), name='get-session-volume'),
    path('get/total/volume/', GetTotalVolumeView.as_view(), name='get-total-volume'),
    path('get/all/volume/', GetAllVolumeView.as_view(), name='get-all-volume'),
]
