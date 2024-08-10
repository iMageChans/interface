from usdt.models import CurrencyProfile
from usdt.serializers import CurrencyProfileSerializer


class PriceRate:
    def __init__(self, validated_data):
        name = validated_data.get('name', None)
        if name is None:
            self.currency_profile = CurrencyProfile.objects.all()
        else:
            self.currency_profile = CurrencyProfile.objects.filter(name=name)

    def serializers(self):
        return CurrencyProfileSerializer(instance=self.currency_profile, many=True).data

    def is_success(self):
        return True
