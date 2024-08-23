from substrateinterface import Keypair


def check_keypair(data):
    if Keypair.validate_mnemonic(data):
        try:
            return Keypair.create_from_mnemonic(data, ss58_format=9)
        except ValueError:
            raise ValueError("ECDSA mnemonic only supports english")
    elif isinstance(data, list):
        try:
            mnemonic = ' '.join(data)
            return Keypair.create_from_mnemonic(mnemonic, ss58_format=9)
        except ValueError:
            raise ValueError("ECDSA mnemonic only supports english")
    elif isinstance(data, str):
        try:
            keypair = Keypair.create_from_private_key(data, ss58_format=9)
        except ValueError:
            keypair = Keypair.create_from_seed(data, ss58_format=9)
        return keypair


class ValidAddress:
    def __init__(self, address):
        self.address = address

    def get_valid_address(self):
        prefix = "Dn"
        if self.address.startswith(prefix):
            # 提取实际地址部分
            actual_address = self.address[len(prefix):]
            try:
                keypair = Keypair(ss58_address=actual_address)
                return actual_address
            except ValueError as e:
                print(f"Invalid address: {e}")
                return None
        else:
            print("Invalid prefix")
            return self.address

    def mate_data_address(self):
        return self.address
