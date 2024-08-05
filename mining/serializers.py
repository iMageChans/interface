from rest_framework import serializers
from mining.models import *
from utils.numbers import DecimalTruncation


class AccumulativeRewardPoolSerializer(serializers.ModelSerializer):
    totals = serializers.SerializerMethodField()

    class Meta:
        model = AccumulativeRewardPool
        fields = ['totals']

    def get_totals(self, obj):
        return DecimalTruncation(2).format_d9(obj.totals)


class MerchantVolumeSerializer(serializers.ModelSerializer):
    totals = serializers.SerializerMethodField()

    class Meta:
        model = MerchantVolume
        fields = ['totals']

    def get_totals(self, obj):
        return DecimalTruncation(2).format_d9(obj.totals)


class SessionVolumeSerializer(serializers.ModelSerializer):
    totals = serializers.SerializerMethodField()

    class Meta:
        model = SessionVolume
        fields = ['totals']

    def get_totals(self, obj):
        return DecimalTruncation(2).format_d9(obj.totals)


class TotalVolumeSerializer(serializers.ModelSerializer):
    totals = serializers.SerializerMethodField()

    class Meta:
        model = TotalVolume
        fields = ['totals']

    def get_totals(self, obj):
        return DecimalTruncation(2).format_d9(obj.totals)


class GetAccumulativeRewardPoolSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)


class GetMerchantVolumeSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)


class GetSessionVolumeSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    session_index = serializers.IntegerField(required=True)


class GetTotalVolumeSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)


class GetAllVolumeSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
