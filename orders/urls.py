from django.urls import path
from .views import (
    D9TransactionView,
)

urlpatterns = [
    # 省级代理接口
    path('d9/transfer/', D9TransactionView.as_view(), name='d9_transfer'),
]