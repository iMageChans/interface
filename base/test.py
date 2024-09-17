from base64 import b64encode, b64decode
from unittest.mock import patch

from substrateinterface.keypair import Keypair

Keypair.generate_mnemonic()


# data = {
#     "mnemonic": "blast curve early try fold fall plastic hobby donkey tomato crater diet",
#     "path": "/1"
# }

# data = "blast curve early try fold fall plastic hobby donkey tomato crater diet"
# patch = '/1'
#
# def get_keypair(mnemonic, path):
#     keypair = Keypair.create_from_uri(mnemonic + path, ss58_format=9)
#     return keypair.ss58_address, keypair.public_key.hex()
#
#
# print(get_keypair(data, patch))

a = Keypair.create_from_mnemonic("act pumpkin off meat display donkey silly add organ choice attitude city", ss58_format=9)
print(a.ss58_address)