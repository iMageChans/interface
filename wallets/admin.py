from django.contrib import admin
from .models import Wallet, WalletTransactionRecord

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('address', 'd9', 'usdt', 'last_login', 'created_at', 'updated_at')
    search_fields = ('address',)
    list_filter = ('created_at', 'updated_at')


@admin.register(WalletTransactionRecord)
class WalletTransactionRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'operation', 'status', 'token', 'amount', 'is_increase', 'created_at', 'updated_at')
    search_fields = ('user', 'operation', 'status')
    list_filter = ('status', 'token', 'created_at', 'is_increase')
