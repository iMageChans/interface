from base.actions import BaseActionsRead
from referrals.service.read import Read


class GetDirectReferralsCount(BaseActionsRead):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.results = Read().direct_referrals_count(self.account_id.get_valid_address())

    def is_success(self):
        return True