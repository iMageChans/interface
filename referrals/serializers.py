from rest_framework import serializers

from base.serializers import KeypairSerializer


class GetDirectReferralsCountSerializer(KeypairSerializer):
    account_id = serializers.CharField(required=False)