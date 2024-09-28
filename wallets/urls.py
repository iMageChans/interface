from django.urls import path
from wallets import views

urlpatterns = [
    path('', views.WalletsView.as_view(), name='wallets'),
    path('d9/balance/', views.D9BalancesView.as_view(), name='d9-balance'),
    path('usdt/balance/', views.USDTBalancesView.as_view(), name='d9-balance'),
]