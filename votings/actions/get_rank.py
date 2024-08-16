from base.actions import BaseActionsRead
from votings.models import Rank
from votings.serializers import RankSerializer


class GetRank(BaseActionsRead):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        rank = Rank.objects.all()
        self.results = RankSerializer(rank, many=True).data

    def serializers(self):
        return self.results

    def is_success(self):
        return True