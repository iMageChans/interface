from django.contrib import admin
from amm.models import *


@admin.register(TokenMarketInformation)
class TokenMarketInformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'd9_token', 'usdt_token', 'd9_rate', 'usdt_rate', )
