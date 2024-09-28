# merchant/models.py

from django.db import models

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    )

    from_address= models.CharField(max_length=100, unique=True, blank=True, null=True)
    to_address= models.CharField(max_length=100, unique=True, blank=True, null=True)
    order_id = models.CharField(max_length=50, unique=True, verbose_name='订单ID')
    operation = models.CharField(max_length=100, verbose_name='交易类型')
    params = models.JSONField(verbose_name='交易参数')
    fee = models.FloatField(default=0, verbose_name='手续费')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='交易状态')
    transaction_result = models.JSONField(null=True, blank=True, verbose_name='交易执行结果')
    error_message = models.TextField(null=True, blank=True, verbose_name='错误信息')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __str__(self):
        return f"Order {self.order_id} - {self.operation} - {self.status}"
