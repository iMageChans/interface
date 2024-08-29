from django.db import models
import uuid
from django.utils import timezone

class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    block_hash = models.CharField(max_length=255, unique=True, db_index=True)
    extrinsic_hash = models.CharField(max_length=255, unique=True, db_index=True)
    total_fee_amount = models.CharField(max_length=255, unique=True)
    block_number = models.IntegerField(db_index=True)
    form_address = models.CharField(max_length=255, unique=True, db_index=True)
    to_address = models.CharField(max_length=255, unique=True, db_index=True)
    usdt = models.CharField(max_length=255, unique=True, default='0', blank=True)
    d9 = models.CharField(max_length=255, unique=True, default='0', blank=True)
    point = models.CharField(max_length=255, unique=True, default='0', blank=True)
    actions = models.CharField(max_length=255, unique=True, db_index=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False, db_index=True)

    def __str__(self):
        return f"{self.id}"
