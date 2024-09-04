from rest_framework import serializers


class GetDirectReferralsCountSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True, write_only=True)
    account_id = serializers.CharField(required=False)