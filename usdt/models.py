from django.db import models


class CurrencyProfile(models.Model):
    name = models.CharField(max_length=50, default="0", blank=True, null=True)
    price = models.CharField(max_length=50, default="0", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
