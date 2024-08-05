from django.urls import path
from referrals.views import *

urlpatterns = [
    path('get/direct/count/', GetDirectReferralsCountView.as_view(), name='get-direct-referrals-count'),
]