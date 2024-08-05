from scalecodec.types import GenericContractExecResult

from base.d9_contracts import D9Contract
from substrateinterface import Keypair
from base import config
from merchant.abi import files


class Read(D9Contract):

    def __init__(self, keypair: Keypair):
        super().__init__(
            contract_address=config.MERCHANT_CONTRACT,
            metadata_file=files.get_abi_files(),
            keypair=keypair
        )

    def get_merchant_expiry(self, account_id: str) -> GenericContractExecResult:
        params = {
            "account_id": account_id,
        }
        return self.contract_read('get_expiry', params)

    def get_user_merchant_profile(self, account_id: str) -> GenericContractExecResult:
        params = {
            "account_id": account_id,
        }
        return self.contract_read('get_account', params)

