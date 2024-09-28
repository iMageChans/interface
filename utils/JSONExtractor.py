from typing import Any, Dict, Optional, Tuple
from utils.token_rate_calculation import DecimalTruncation
import datetime
import numbers  # Ensure this is correctly imported or defined

class JSONExtractor:
    def extract_last_ok(self, data: Any) -> Tuple[Optional[Any], bool]:
        if isinstance(data, dict):
            for key, value in data.items():
                if key == "Ok":
                    return self.extract_last_ok(value)[0], True
                elif key == "Err":
                    return self.extract_last_ok(value)[0], False
                else:
                    result, status = self.extract_last_ok(value)
                    if result is not None and result != value:
                        return result, status
        elif isinstance(data, (list, tuple)):
            for item in data:
                result, status = self.extract_last_ok(item)
                if result is not None:
                    return result, status
        elif isinstance(data, (int, str, float)):
            return data, False
        return None, False

    def estimate_exchange_rate_usdt_to_d9(self, data: Any) -> Optional[Dict[str, str]]:
        keys = ['usdt', 'd9']
        value, checks = self.extract_last_ok(data)
        if value and isinstance(value, (list, tuple)) and len(value) == 2:
            data_dict = dict(zip(keys, value))
            data_dict['usdt'] = DecimalTruncation(2).format_usdt(data_dict['usdt'])
            data_dict['d9'] = DecimalTruncation(2).format_d9(data_dict['d9'])
            if checks:
                return data_dict
        return None

    def estimate_exchange_rate_d9_to_usdt(self, data: Any) -> Optional[Dict[str, str]]:
        keys = ['d9', 'usdt']
        value, checks = self.extract_last_ok(data)
        if value and isinstance(value, (list, tuple)) and len(value) == 2:
            data_dict = dict(zip(keys, value))
            data_dict['usdt'] = DecimalTruncation(2).format_usdt(data_dict['usdt'])
            data_dict['d9'] = DecimalTruncation(2).format_d9(data_dict['d9'])
            if checks:
                return data_dict
        return None

    def d9_to_usdt(self, data: Any) -> Optional[Dict[str, Any]]:
        if data is None:
            return None
        value, checks = self.extract_last_ok(data)
        if checks and isinstance(value, (list, tuple)) and len(value) == 2:
            return {'d9': value[0], 'usdt': value[1]}
        return None

    def usdt_to_d9(self, data: Any) -> Optional[Dict[str, Any]]:
        if data is None:
            return None
        value, checks = self.extract_last_ok(data)
        if checks and isinstance(value, (list, tuple)) and len(value) == 2:
            return {'usdt': value[0], 'd9': value[1]}
        return None

    def get_data_or_err(self, data: Any) -> Optional[Any]:
        value, checks = self.extract_last_ok(data)
        return value if checks else None

    @staticmethod
    def get_balances_d9(data: Any) -> Optional[Any]:
        if data and hasattr(data, 'value_serialized'):
            return data.value_serialized.get('data', {}).get('free')
        return None

    @staticmethod
    def get_transfer_data(data: Any) -> Optional[Dict[str, Any]]:
        if data and hasattr(data, 'block_hash') and hasattr(data, 'extrinsic_hash') and hasattr(data, 'total_fee_amount'):
            return {
                "block_hash": data.block_hash,
                "extrinsic_hash": data.extrinsic_hash,
                "total_fee_amount": DecimalTruncation(7).format_d9(data.total_fee_amount),
            }
        return None

    @staticmethod
    def get_burning_portfolio(data: Dict[str, Any]) -> Dict[str, Any]:
        result = data.get('result', {}).get('Ok', {}).get('data', {}).get('Ok', {})
        if result:
            return {
                "amount_burned": DecimalTruncation(2).format_d9(result.get('amount_burned', 0)),
                "balance_due": DecimalTruncation(2).format_d9(result.get('balance_due', 0)),
                "balance_paid": DecimalTruncation(2).format_d9(result.get('balance_paid', 0)),
                "last_withdrawal": result.get('last_withdrawal', {}).get('time', 0),
                "last_burn": result.get('last_burn', {}).get('time', 0),
            }
        else:
            return {
                "amount_burned": "0",
                "balance_due": "0",
                "balance_paid": "0",
                "last_withdrawal": 0,
                "last_burn": 0,
            }

    @staticmethod
    def get_merchant_portfolio(data: Dict[str, Any]) -> Dict[str, Any]:
        result = data.get('result', {}).get('Ok', {}).get('data', {}).get('Ok', {})
        if result:
            timestamp = result.get('last_conversion', 0)
            dt = datetime.datetime.fromtimestamp(timestamp / 1000)
            now = datetime.datetime.now()
            days_difference = (now - dt).days
            redeemed_usdt = DecimalTruncation(2).format_usdt(
                (result.get('green_points', 0) + sum(result.get('relationship_factors', [0, 0]))) * 0.0005 / 100 * days_difference
            )

            return {
                "green_points": DecimalTruncation(2).format_usdt(result.get('green_points', 0)),
                "relationship_green_points": DecimalTruncation(2).format_usdt(result.get('green_points', 0) * 0.0005),
                "relationship_red_points": DecimalTruncation(2).format_usdt(
                    sum(result.get('relationship_factors', [0, 0]))
                ),
                "last_conversion": timestamp,
                "redeemed_usdt": redeemed_usdt,
                "redeemed_d9": DecimalTruncation(2).format_d9(result.get('redeemed_d9', 0)),
                "created_at": result.get('created_at', 0),
            }
        else:
            return {
                "green_points": "0",
                "relationship_green_points": "0",
                "relationship_red_points": "0",
                "last_conversion": 0,
                "redeemed_usdt": "0",
                "redeemed_d9": "0",
                "created_at": 0,
            }
