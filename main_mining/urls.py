from django.urls import path
from main_mining.views import *

urlpatterns = [
    path('get/total/burned/', GetTotalBurnedView.as_view(), name='get-total-burned'),
    path('get/user/burning/profile/', GetUserBurningProfileView.as_view(), name='get-user-burning-profile'),
    path('burning/', BurningView.as_view(), name='user-burning'),
    path('withdraw/', WithdrawView.as_view(), name='user-withdraw'),
    path('get/return/percent/', GetReturnPercentView.as_view(), name='get-return-percent'),
]