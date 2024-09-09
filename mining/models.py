from django.db import models
from django.utils import timezone


class AccumulativeRewardPool(models.Model):
    totals = models.CharField(max_length=255, default="0", blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f"{self.totals}"


class MerchantVolume(models.Model):
    totals = models.CharField(max_length=255, default="0", blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f"{self.totals}"


class SessionVolume(models.Model):
    totals = models.CharField(max_length=255, default="0", blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f"{self.totals}"


class TotalVolume(models.Model):
    totals = models.CharField(max_length=255, default="0", blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f"{self.totals}"
