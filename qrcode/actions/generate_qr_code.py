from utils import keystone
from django.http import HttpRequest
from urllib.parse import urlencode


class GenerateQRCode:
    def __init__(self, request: HttpRequest, validated_data):
        keypair = keystone.check_keypair(validated_data['keypair'])
        amount = validated_data['amount']
        base_url = request.build_absolute_uri('/api/qrcode/process/')
        data = {
            "account_id": f"Dn{keypair.ss58_address}",
            "amount": amount,
        }
        query_params = urlencode(data)
        self.qr_code_link = f"{base_url}?{query_params}"

    def serializers(self):
        return self.qr_code_link

    def is_success(self):
        return True
