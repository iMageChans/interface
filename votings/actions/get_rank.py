from base.actions import BaseActionsRead
from votings.models import Rank
from votings.serializers import RankSerializer


class GetRank(BaseActionsRead):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.results = Rank.objects.all()

    def serializers(self):
        return RankSerializer(self.results, many=True).data

    def is_success(self):
        return True