# merchant/urls.py

from django.urls import path
from merchant import views

urlpatterns = [
    path('subscribe/', views.SubscribeView.as_view(), name='subscribe'),
    path('redeem_d9/', views.RedeemD9View.as_view(), name='redeem_d9'),
    path('give_points_d9/', views.GivePointsD9View.as_view(), name='give_points_d9'),
    path('give_points_usdt/', views.GivePointsUSDTView.as_view(), name='give_points_usdt'),
    path('send_usdt_payment/', views.SendUSDTPaymentToMerchantView.as_view(), name='send_usdt_payment'),
    path('send_d9_payment/', views.SendD9PaymentToMerchantView.as_view(), name='send_d9_payment'),
]
