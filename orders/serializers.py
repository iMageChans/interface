from rest_framework import serializers

class BaseTransferSerializer(serializers.Serializer):
    from_address = serializers.CharField(required=False, allow_null=True)
    to_address = serializers.CharField(required=True)
    amount = serializers.FloatField(required=True)


class D9TransferSerializer(BaseTransferSerializer):
    pass