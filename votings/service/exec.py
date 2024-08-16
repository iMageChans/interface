from base import config
from base.d9_pallets import D9PalletsExec


class Exec(D9PalletsExec):
    def __init__(self):
        super().__init__('D9NodeVoting')

    def add_voting_interest(self, beneficiary_voter: str, amount_to_burn: int):
        """
        adds voting interest
        Args:
            beneficiary_voter: beneficiary voter
            amount_to_burn: amount to burn in base units
        Returns:
        GenericCall
          """
        func_params = {
            'beneficiary_voter': beneficiary_voter,
            'main_pool': config.MAIN_MINING_CONTRACT,
            'amount_to_burn': amount_to_burn,
            'burn_contract': config.BURN_MINING_CONTRACT
        }
        return self.compose_call('add_voting_interest', func_params)

    def change_candidate_name(self, name: str):
        """
        changes candidate name
        Args:
            name (str): name in hexadecimal format
        Returns:
            GenericCalls
            """
        return self.compose_call("change_candidate_name", {'name': name})

    def change_candidate_support_share(self, percent: int):
        """
        changes candidate support share
        Args:
            percent (int): percent
        Returns:
            GenericCall
          """
        if percent > 100 or percent < 0:
            raise ValueError("percent must be between 0 and 100")
        return self.compose_call("change_candidate_supporter_share", {'sharing_percent': percent})

    def delegate_votes(self, delegations):
        """
        delegates votes
        Args:
            delegations (List[Delegation]): delegations
        Returns:
            GenericCall
          """
        return self.compose_call("delegate_votes", {'delegations': delegations})

    def redistribute_votes(self, from_candidate: str, to_candidate: str):
        """
        redistribute votes
        Args:
            from_candidate (str): from candidate
            to_candidate (str): to candidate
        Returns:
            GenericCall
           """
        return self.compose_call("redistribute_votes", {'from': from_candidate, 'to': to_candidate})

    def remove_candidacy(self):
        """
        removes candidacy
        Args:
            candidate_id (str): candidate id
        Returns:
            GenericCall
          """
        return self.compose_call("RemoveCandidacy")

    def try_remove_votes_from_candidate(self, candidate: str, votes: int):
        return self.compose_call("try_remove_votes_from_candidate", {'candidate': candidate, 'votes': votes})