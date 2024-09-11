from base64 import b64encode, b64decode
from substrateinterface.keypair import Keypair

Keypair.generate_mnemonic()


# data = {
#     "mnemonic": "blast curve early try fold fall plastic hobby donkey tomato crater diet",
#     "path": "/1"
# }

data = "blast curve early try fold fall plastic hobby donkey tomato crater diet, /1"

print(b64decode(data))