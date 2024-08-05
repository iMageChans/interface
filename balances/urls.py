from django.urls import path
from balances.views import *

urlpatterns = [
    path('get/', GetBalancesView.as_view(), name='get-balances'),
    path('transfers/', TransfersView.as_view(), name='d9-transfers'),
]
