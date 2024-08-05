from django.db import models


class Rank(models.Model):
    node_id = models.CharField(max_length=255)
    node_name = models.CharField(max_length=255)
    sharing_percent = models.IntegerField()
    accumulative_votes = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-accumulative_votes']
        verbose_name_plural = 'Ranks'
