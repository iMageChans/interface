from django.urls import path
from merchant.views import *

urlpatterns = [
    path('get/merchant/expiry/', GetMerchantExpiryView.as_view(), name='get-merchant-expiry'),
    path('get/user/profile/', GetUserMerchantProfileView.as_view(), name='get-user-merchant-profile'),
    path('subscribe/', SubscribeView.as_view(), name='merchant-subscribe'),
    path('redeem/d9/', RedeemD9View.as_view(), name='merchant-redeem-d9'),
    path('give/point/d9/', GivePointsD9View.as_view(), name='give-point-d9'),
    path('give/point/usdt/', GivePointsUSDTView.as_view(), name='give-point-usdt'),
    path('send/d9/payment/', SendD9PaymentToMerchantView.as_view(), name='send-d9-payment'),
    path('send/usdt/payment/', SendUSDTPaymentToMerchantView.as_view(), name='send-usdt-payment'),
]