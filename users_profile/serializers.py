from rest_framework import serializers

from base.serializers import KeypairSerializer
from users_profile.models import UserBalances, USDTBalances, UserBurningProfile, MerchantExpiry, UserMerchantProfile, \
    UserToNodeVote


class GetUserToNodeVoteSerializer(KeypairSerializer):
    account_id = serializers.CharField(required=True)


class UserToNodeVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserToNodeVote
        exclude = ['id', 'account_id']


class UserMerchantProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMerchantProfile
        exclude = ['account_id']


class MerchantExpirySerializer(serializers.ModelSerializer):
    class Meta:
        model = MerchantExpiry
        fields = ['expiry_date']


class UserBurningProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBurningProfile
        exclude = ['account_id']


class UserBalancesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBalances
        fields = ['balance_d9']


class USDTBalancesSerializer(serializers.ModelSerializer):
    class Meta:
        model = USDTBalances
        fields = ['balance_usdt']


class UsersProfileSerializer(KeypairSerializer):
    pass
