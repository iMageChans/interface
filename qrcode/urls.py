from django.urls import path
from qrcode.views import *

urlpatterns = [
    path('generate/', GenerateQRCodeView.as_view(), name='generate-qrcode'),
    path('process/', ProcessQRCodeView.as_view(), name='generate-qrcode'),
]