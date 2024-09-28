from django.db import models

import uuid
from django.db import models
from django.utils import timezone

class Wallet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address = models.CharField(max_length=100, unique=True)
    d9 = models.DecimalField(max_digits=24, decimal_places=12, default=0)
    usdt = models.DecimalField(max_digits=20, decimal_places=12, default=0)
    last_login = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address


class WalletTransactionRecord(models.Model):
    user = models.CharField(max_length=100)
    operation = models.CharField(max_length=100)
    params = models.JSONField()
    status = models.CharField(max_length=20, choices=(
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed'),
    ), default='pending')
    token = models.CharField(max_length=20, choices=(
        ('d9', 'D9'),
        ('usdt', 'USDT'),
    ))
    amount = models.DecimalField(max_digits=20, decimal_places=10, default=0)
    is_increase = models.BooleanField(default=True,
                                      help_text="Indicates if this is an increase (True) or decrease (False).")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} {self.operation} {self.status}'