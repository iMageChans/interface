from rest_framework import serializers


class RoundedFloatField(serializers.FloatField):
    def __init__(self, **kwargs):
        self.decimals = kwargs.pop('decimals', 2)
        super().__init__(**kwargs)

    def to_representation(self, value):
        value = super().to_representation(value)
        return round(value, self.decimals)
