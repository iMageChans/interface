from utils import keystone
from django.http import HttpRequest
from urllib.parse import urlencode


class GenerateQRCode:
    def __init__(self, request: HttpRequest, validated_data):
        keypair = keystone.check_keypair(validated_data['keypair'])
        amount = validated_data['amount']
        type = validated_data['type']
        base_url = request.build_absolute_uri('/api/qrcode/process/')
        if base_url.startswith('http://'):
            base_url = base_url.replace('http://', 'https://', 1)
        data = {
            "account_id": f"Dn{keypair.ss58_address}",
            "amount": amount,
            "type": type,
        }
        query_params = urlencode(data)
        self.qr_code_link = f"{base_url}?{query_params}"

    def serializers(self):
        return self.qr_code_link

    def is_success(self):
        return True
