from django.contrib import admin
from users_profile.models import *


@admin.register(UserToNodeVote)
class UserToNodeVoteAdmin(admin.ModelAdmin):
    list_display = ('account_id', 'node_id', 'node_name', 'vote')


@admin.register(MerchantExpiry)
class MerchantExpiryAdmin(admin.ModelAdmin):
    list_display = ('account_id', 'expiry_date', 'created_at')


@admin.register(UserBurningProfile)
class UserBurningProfileAdmin(admin.ModelAdmin):
    list_display = ('account_id', 'amount_burned', 'balance_due', 'balance_paid', 'last_withdrawal', 'last_burn')


@admin.register(UserMerchantProfile)
class UserMerchantProfileAdmin(admin.ModelAdmin):
    list_display = (
    'account_id', 'created_at', 'relationship_green_points', 'relationship_red_points', 'last_conversion',
    'redeemed_usdt', 'redeemed_d9', 'created_at')


@admin.register(UserBalances)
class UserBalancesAdmin(admin.ModelAdmin):
    list_display = ('account_id', 'created_at', 'balance_d9',)


@admin.register(USDTBalances)
class USDTBalancesAdmin(admin.ModelAdmin):
    list_display = ('account_id', 'created_at', 'balance_usdt',)
