from base.views import BaseView
from mining import serializers
from mining import actions


class GetAccumulativeRewardPoolView(BaseView):
    serializer_class = serializers.GetAccumulativeRewardPoolSerializer
    action_class = actions.GetAccumulativeRewardPool


class GetMerchantVolumeView(BaseView):
    serializer_class = serializers.GetMerchantVolumeSerializer
    action_class = actions.GetMerchantVolume


class GetSessionVolumeView(BaseView):
    serializer_class = serializers.GetSessionVolumeSerializer
    action_class = actions.GetSessionVolume


class GetTotalVolumeView(BaseView):
    serializer_class = serializers.GetTotalVolumeSerializer
    action_class = actions.GetTotalVolume


class GetAllVolumeView(BaseView):
    serializer_class = serializers.GetAllVolumeSerializer
    action_class = actions.GetAllVolume
