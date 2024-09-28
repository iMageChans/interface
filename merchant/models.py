from django.db import models

class TransactionRecord(models.Model):
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

