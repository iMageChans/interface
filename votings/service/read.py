from scalecodec.base import ScaleType

from base.d9_pallets import D9PalletsRead


class Read(D9PalletsRead):
    def __init__(self):
        super().__init__('D9NodeVoting')

    def get_number_of_candidates(self):
        """
        gets number of candidates
        Returns:
            int: number of candidates
        """
        result = self.compose_query('CurrentNumberOfCandidatesNodes', [])
        return result.value_serialized

    def current_session_index(self):
        """
        gets current session index
        Returns:
            int: current session index
        """
        result = self.compose_query('CurrentSessionIndex', [])
        return result.value_serialized

    def validator_stats(self, validator_id: str):
        """
        gets validator stats
        Returns:
            dict: validator stats
        """
        result = self.compose_query('CurrentValidatorVoteStats', [validator_id])
        return result.value_serialized

    def get_node_accumulative_votes(self, node_id: str):
        """
        gets node accumulative votes
        Returns:
            dict: node accumulative votes
        """
        result = self.compose_query('NodeAccumulativeVotes', [node_id])
        return result.value_serialized

    def users_voting_interests(self, account_id: str):
        """
        gets node metadata
        Returns:
            dict: node metadata
        """
        result = self.compose_query('usersVotingInterests', [account_id])
        return result.value_serialized


    def get_node_metadata(self, node_id: str):
        """
        gets node metadata
        Returns:
            dict: node metadata
        """
        result = self.compose_query('NodeMetadata', [node_id])
        return result.value_serialized

    def node_to_user_vote_totals(self, node_id: str, user_id: str | None = None):
        """
        gets node to user vote totals
        Returns:
            list: (supporter_id, votes)
        """
        result = self.d9_interface.query_map('D9NodeVoting', 'NodeToUserVotesTotals')
        node_supporters = []
        if user_id == None:
            for node_user_tuple, votes in result:
                if node_user_tuple[0].value == node_id:
                    node_supporters.append((node_user_tuple[1].value, votes.value))
            return node_supporters
        else:
            result = self.compose_query('NodeToUserVotesTotals', [node_id, user_id])
            return result.value_serialized

    def get_session_node_list(self, session_index: int):
        """
        gets session node list
        Returns:
            list: nodes
        """
        result = self.compose_query('SessionNodeList', [session_index])
        return result.value_serialized
