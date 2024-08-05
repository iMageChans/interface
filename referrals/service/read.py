from base.d9_pallets import D9PalletsRead


class Read(D9PalletsRead):
    def __init__(self):
        super().__init__('D9Referral')

    def direct_referrals_count(self, account_id: str):
        """
        gets direct referrals count from chain
        Args:
             account_id (str): account address
        Returns:
             int: direct referrals count
        """
        return self.compose_query('DirectReferralsCount', [account_id])
