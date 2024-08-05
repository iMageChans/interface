from votings.service.read import Read
from votings.models import Rank


def update_or_created_rank():
    read = Read()
    numbers = read.get_number_of_candidates()
    nodes = read.get_session_node_list(numbers)

    for node in nodes:
        node_metadata = read.get_node_metadata(node_id=node)
        node_accumulative_votes = read.get_node_accumulative_votes(node_id=node)

        data = {
            "node_id": "Dn" + node,
            "node_name": node_metadata['name'],
            "sharing_percent": node_metadata['sharing_percent'],
            "accumulative_votes": node_accumulative_votes,
        }

        ranks, created = Rank.objects.update_or_create(
            node_id=data['node_id'],
            defaults=data
        )

        # print({"node_id": ranks.node_id, "node_name": ranks.node_name, "sharing_percent": ranks.sharing_percent,
        #        "accumulative_votes": ranks.accumulative_votes, "created": created})
