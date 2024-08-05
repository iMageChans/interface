from base.views import BaseView
from merchant import serializers
from merchant import actions


class GetMerchantExpiryView(BaseView):
    serializer_class = serializers.GetMerchantExpirySerializer
    action_class = actions.GetMerchantExpiry


class GetUserMerchantProfileView(BaseView):
    serializer_class = serializers.GetUserMerchantProfileSerializer
    action_class = actions.GetUserMerchantProfile


class SubscribeView(BaseView):
    serializer_class = serializers.SubscribeSerializer
    action_class = actions.Subscribe


class RedeemD9View(BaseView):
    serializer_class = serializers.RedeemD9Serializer
    action_class = actions.RedeemD9


class GivePointsD9View(BaseView):
    serializer_class = serializers.GivePointsD9Serializer
    action_class = actions.GivePointsD9


class GivePointsUSDTView(BaseView):
    serializer_class = serializers.GivePointsUSDTSerializer
    action_class = actions.GivePointsUSDT


class SendUSDTPaymentToMerchantView(BaseView):
    serializer_class = serializers.USDTPaymentSerializer
    action_class = actions.SendUSDTPaymentToMerchant


class SendD9PaymentToMerchantView(BaseView):
    serializer_class = serializers.D9PaymentSerializer
    action_class = actions.SendD9PaymentToMerchant
