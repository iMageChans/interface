from base.actions import BaseActionsRead
from main_mining import celery
from utils import numbers


class GetReturnPercent(BaseActionsRead):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        total_burned = celery.update_or_created_total_burned()
        self.results = total_burned.totals

    def serializers(self):
        values = numbers.DecimalTruncation(0).format_d9(self.results)
        return numbers.get_return_percent(values)

    def is_success(self):
        return True