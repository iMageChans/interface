from django.db import models
from django.utils import timezone


class UserToNodeVote(models.Model):
    account_id = models.CharField(max_length=255)
    node_id = models.CharField(max_length=255)
    node_name = models.CharField(max_length=255)
    vote = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.account_id}"


class UserMerchantProfile(models.Model):
    account_id = models.CharField(max_length=255, primary_key=True)
    green_points = models.CharField(max_length=255)
    # relationship_factors = ArrayField(models.CharField(max_length=255))
    relationship_green_points = models.CharField(max_length=255, default="0")
    relationship_red_points = models.CharField(max_length=255, default="0")
    last_conversion = models.CharField(max_length=255)
    redeemed_usdt = models.CharField(max_length=255)
    redeemed_d9 = models.CharField(max_length=255)
    created_at = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.account_id}"


class MerchantExpiry(models.Model):
    account_id = models.CharField(max_length=255, primary_key=True)
    expiry_date = models.CharField(max_length=255, default="1567958400")
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f"{self.account_id}"


class UserBalances(models.Model):
    account_id = models.CharField(max_length=255, primary_key=True)
    balance_d9 = models.CharField(max_length=255, default="0", blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f"{self.account_id}"


class USDTBalances(models.Model):
    account_id = models.CharField(max_length=255, primary_key=True)
    balance_usdt = models.CharField(max_length=255, default="0", blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f"{self.account_id}"


class UserBurningProfile(models.Model):
    account_id = models.CharField(max_length=255, primary_key=True)
    amount_burned = models.CharField(max_length=255, default="0", blank=True, null=True)
    balance_due = models.CharField(max_length=255, default="0", blank=True, null=True)
    balance_paid = models.CharField(max_length=255, default="0", blank=True, null=True)
    last_withdrawal = models.CharField(max_length=255, default="0", blank=True, null=True)
    last_burn = models.CharField(max_length=255, default="0", blank=True, null=True)

    def __str__(self):
        return f"{self.account_id}"
