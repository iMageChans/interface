from base.actions import BaseActionsRead
from main_mining.service.read import Read
from utils.JSONExtractor import JSONExtractor


class GetUserBurningProfile(BaseActionsRead):
    def __init__(self, validated_data):
        super().__init__(validated_data)

        main_read = Read(self.keypair)
        self.results = main_read.get_portfolio(self.account_id.get_valid_address())

    def serializers(self):
        return JSONExtractor().get_burning_portfolio(self.results.value_serialized)

    def is_success(self):
        return True