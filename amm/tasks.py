from substrateinterface import Keypair
from celery import shared_task
from amm import celery
from amm.service.read import Read
from amm.serializers import *
from utils.JSONExtractor import extractor


@shared_task
def update_or_created_token_market_information_celery():
    mnemonic = Keypair.generate_mnemonic()
    keypair = Keypair.create_from_mnemonic(mnemonic, ss58_format=9)
    read = Read(keypair).get_reserves()
    data = extractor.d9_to_usdt(read.value_serialized)
    token_market_information = celery.update_or_created_token_market_information(data)
    print("update_or_created_token_market_information:", TokenMarketInformationSerializer(token_market_information).data)