from base.actions import BaseActionsRead
from mining import models
from mining import serializers


class GetTotalVolume(BaseActionsRead):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.results = models.TotalVolume.objects.order_by('-created_at').first()

    def serializers(self):
        return serializers.TotalVolumeSerializer(self.results).data

    def is_success(self):
        if self.results:
            return True
        return False
