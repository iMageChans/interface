from votings.service.read import Read
from users_profile.models import UserToNodeVote


def update_or_created_node_user_vote():
    read = Read()
    numbers = read.get_number_of_candidates()
    nodes = read.get_session_node_list(numbers)

    for node in nodes:
        node_metadata = read.get_node_metadata(node_id=node)
        node_to_user_vote = read.node_to_user_vote_totals(node_id=node)
        for user in node_to_user_vote:
            data = {
                "node_id": "Dn" + node,
                "node_name": node_metadata['name'],
                "account_id": f"Dn{user[0]}",
                "vote": user[1]
            }

            UserToNodeVote.objects.update_or_create(
                account_id=data["account_id"],
                node_id=data["node_id"],
                defaults=data
            )
