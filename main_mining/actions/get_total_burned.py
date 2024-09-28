from base.actions import BaseActionsRead
from main_mining import celery
from utils.token_rate_calculation import DecimalTruncation


class GetTotalBurned(BaseActionsRead):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        total_burned = celery.update_or_created_total_burned()
        self.results = total_burned.totals

    def serializers(self):
        values = DecimalTruncation(4).format_d9(self.results)
        return values

    def is_success(self):
        if self.results is not None:
            return True
        return False