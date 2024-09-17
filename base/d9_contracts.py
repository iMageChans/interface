from scalecodec.types import GenericCall
from base.config import PYTHON_MAIN_NET_URL
from substrateinterface.contracts import ContractInstance
from substrateinterface import Keypair, SubstrateInterface
from dogpile.cache import make_region
from typing import Optional


region = make_region().configure(
    'dogpile.cache.memory',
    expiration_time=3600,
)


class D9Contract:
    def __init__(self, contract_address: str, metadata_file: str, keypair: Keypair):
        self.keypair = keypair
        self.substrate = substrate = SubstrateInterface(
            url=PYTHON_MAIN_NET_URL,
            ss58_format=9,
            type_registry_preset='polkadot',
            auto_discover=False,
            use_remote_preset=False,
            auto_reconnect=True,
        )
        self.contract = ContractInstance.create_from_address(
            contract_address=contract_address,
            metadata_file=metadata_file,
            substrate=self.substrate,
        )

    def get_block_number(self, block_hash: str) -> int:
        """
        获取指定区块哈希的区块号。

        参数：
            block_hash (str): 区块哈希。

        返回：
            int: 区块号。
        """
        return self.contract.substrate.get_block_number(block_hash=block_hash)

    def contract_exec(
            self,
            call_name: str,
            call_params: Optional[dict] = None,
            value: int = 0
    ):
        """
        执行会改变合约状态的函数。

        参数：
            call_name (str): 合约函数名。
            call_params (Optional[dict]): 合约函数参数。
            value (int): 调用时转移的值。

        返回：
            执行结果。
        """
        result = self.contract.exec(self.keypair, call_name, call_params, value)
        return result

    def contract_read(
            self,
            call_name: str,
            call_params: Optional[dict] = None,
            value: int = 0
    ):
        """
        读取合约数据，不改变状态。

        参数：
            call_name (str): 合约函数名。
            call_params (Optional[dict]): 合约函数参数。
            value (int): 调用时转移的值。

        返回：
            读取结果。
        """
        result = self.contract.read(self.keypair, call_name, call_params, value)
        return result

    def contract_call(
            self,
            call_name: str,
            call_params: Optional[dict] = None,
            value: int = 0
    ):
        """
        组装合约调用。

        参数：
            call_name (str): 合约函数名。
            call_params (Optional[dict]): 合约函数参数。
            value (int): 调用时转移的值。

        返回：
            GenericCall: 组装的调用对象。
        """
        return self.call(self.keypair, call_name, call_params, value)

    def contract_get_payment_info(
            self,
            call_name: str,
            call_params: Optional[dict] = None,
            value: int = 0
    ):
        """
        获取合约调用的支付信息。

        参数：
            call_name (str): 合约函数名。
            call_params (Optional[dict]): 合约函数参数。
            value (int): 调用时转移的值。

        返回：
            支付信息。
        """
        return self.get_payment_info(self.keypair, call_name, call_params, value)

    def get_payment_info(
            self,
            keypair: Keypair,
            method: str,
            args: Optional[dict] = None,
            value: int = 0,
            gas_limit: Optional[dict] = None,
            storage_deposit_limit: Optional[int] = None
    ):
        """
        计算合约调用的支付信息。

        参数：
            keypair (Keypair): 调用者的密钥对。
            method (str): 合约方法名。
            args (Optional[dict]): 方法参数。
            value (int): 调用时转移的值。
            gas_limit (Optional[dict]): Gas限制。
            storage_deposit_limit (Optional[int]): 存储押金限制。

        返回：
            支付信息。
        """
        if gas_limit is None:
            gas_predict_result = self.contract.read(keypair, method, args, value)
            gas_limit = gas_predict_result.gas_required

        input_data = self.contract.metadata.generate_message_data(
            name=method, args=args
        )

        call = self.contract.substrate.compose_call(
            call_module='Contracts',
            call_function='call',
            call_params={
                'dest': self.contract.contract_address,
                'value': value,
                'gas_limit': gas_limit,
                'storage_deposit_limit': storage_deposit_limit,
                'data': input_data.to_hex(),
            },
        )

        return self.contract.substrate.get_payment_info(call=call, keypair=keypair)

    def call(
            self,
            keypair: Keypair,
            method: str,
            args: Optional[dict] = None,
            value: int = 0,
            gas_limit: Optional[dict] = None,
            storage_deposit_limit: Optional[int] = None
    ) -> GenericCall:
        """
        组装合约方法的调用对象。

        参数：
            keypair (Keypair): 调用者的密钥对。
            method (str): 合约方法名。
            args (Optional[dict]): 方法参数。
            value (int): 调用时转移的值。
            gas_limit (Optional[dict]): Gas限制。
            storage_deposit_limit (Optional[int]): 存储押金限制。

        返回：
            GenericCall: 组装的调用对象。
        """
        input_data = self.contract.metadata.generate_message_data(
            name=method, args=args
        )
        return self.contract.substrate.compose_call(
            call_module='Contracts',
            call_function='call',
            call_params={
                'dest': self.contract.contract_address,
                'value': value,
                'gas_limit': gas_limit,
                'storage_deposit_limit': storage_deposit_limit,
                'data': input_data.to_hex(),
            },
        )
