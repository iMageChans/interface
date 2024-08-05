from base.views import *
from qrcode import serializers
from qrcode import actions


class GenerateQRCodeView(BasePOSTView):
    serializer_class = serializers.GenerateQRCodeSerializer
    action_class = actions.GenerateQRCode


class ProcessQRCodeView(BaseGETView):
    serializer_class = serializers.ProcessQRCodeSerializer
