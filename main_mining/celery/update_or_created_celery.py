from substrateinterface import Keypair
from main_mining.service.read import Read
from main_mining.models import *
from utils.JSONExtractor import JSONExtractor


def update_or_created_total_burned():
    mnemonic = Keypair.generate_mnemonic()
    keypair = Keypair.create_from_mnemonic(mnemonic)

    read = Read(keypair).get_total_burned()
    res = JSONExtractor().get_data_or_err(read.value_serialized)

    data = dict()
    data.update({"totals": res})

    total_burned = TotalBurned.objects.order_by("-created_at").first()
    if total_burned is not None:
        if total_burned.totals == str(res):
            return total_burned
        else:
            total_burned = TotalBurned.objects.update_or_create(**data)
            return total_burned
    else:
        total_burned = TotalBurned.objects.update_or_create(**data)
        return total_burned
