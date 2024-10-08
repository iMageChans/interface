from django.db import models
from django.utils import timezone


class TokenMarketInformation(models.Model):
    id = models.AutoField(primary_key=True)
    d9_token = models.CharField(max_length=255, default="0", blank=True, null=True)
    usdt_token = models.CharField(max_length=255, default="0", blank=True, null=True)
    d9_rate = models.FloatField(default=0.00, blank=True, null=True)
    usdt_rate = models.FloatField(default=0.00, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f'Transaction {self.id}: D9 - {self.d9_token}, USDT - {self.usdt_token}'


class LiquidityProvider(models.Model):
    account_id = models.CharField(max_length=255, primary_key=True)
    d9_token = models.CharField(max_length=255, default="0",null=True, blank=True)
    usdt_token = models.CharField(max_length=255, default="0",null=True, blank=True)
    provider = models.FloatField(default=0.00, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.account_id
