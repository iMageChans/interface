from django.db import models
from django.utils import timezone


class TotalBurned(models.Model):
    id = models.AutoField(primary_key=True)
    totals = models.CharField(max_length=200, default="0", blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f'TotalBurned {self.id}: totals - {self.totals}'
