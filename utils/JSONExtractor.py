from utils.token_rate_calculation import *
import datetime


class JSONExtractor:

    def __init__(self):
        self.checks = False

    def extract_last_ok(self, data):
        if isinstance(data, dict):
            for key, value in data.items():
                if key == "Ok":
                    self.checks = True
                    return self.extract_last_ok(value)
                elif key == "Err":
                    self.checks = False
                    return self.extract_last_ok(value)
                else:
                    result = self.extract_last_ok(value)
                    if result is not None and result != value:
                        return result
        elif isinstance(data, (dict, list, tuple, int, str)):
            return data
        return None

    def estimate_exchange_rate_usdt_to_d9(self, data):
        keys = ['usdt', 'd9']
        value = self.extract_last_ok(data)
        data = dict(zip(keys, value))
        data['usdt'] = numbers.DecimalTruncation(2).format_usdt(data['usdt'])
        data['d9'] = numbers.DecimalTruncation(2).format_d9(data['d9'])
        if self.checks:
            return data
        return value

    def estimate_exchange_rate_d9_to_usdt(self, data):
        keys = ['d9', 'usdt']
        value = self.extract_last_ok(data)
        data = dict(zip(keys, value))
        data['usdt'] = numbers.DecimalTruncation(2).format_usdt(data['usdt'])
        data['d9'] = numbers.DecimalTruncation(2).format_d9(data['d9'])
        if self.checks:
            return data
        return value

    def d9_to_usdt(self, data):
        keys = ['d9', 'usdt']
        value = self.extract_last_ok(data)
        if self.checks:
            return dict(zip(keys, value))
        return value

    def usdt_to_d9(self, data):
        keys = ['usdt', 'd9']
        value = self.extract_last_ok(data)
        if self.checks:
            return dict(zip(keys, value))
        return value

    def get_data_or_err(self, data):
        value = self.extract_last_ok(data)
        if self.checks:
            return value
        return value

    def get_balances_d9(self, data):

        if data is not None:
            self.checks = True
        self.checks = False

        return data.value_serialized['data']['free']

    def get_transfer_data(self, data):

        if data is not None:
            self.checks = True
        self.checks = False

        return {
            "block_hash": data.block_hash,
            "extrinsic_hash": data.extrinsic_hash
        }

    def get_burning_portfolio(self, data):

        if isinstance(data, dict):
            self.checks = True
        self.checks = False
        data = data.get('result', {}).get('Ok', {}).get('data', {})
        res = data['Ok']

        if res:
            return {
                "amount_burned": numbers.DecimalTruncation(2).format_d9(res['amount_burned']),
                "balance_due": numbers.DecimalTruncation(2).format_d9(res['balance_due']),
                "balance_paid": numbers.DecimalTruncation(2).format_d9(res['balance_paid']),
                "last_withdrawal": res['last_withdrawal']['time'],
                "last_burn": res['last_burn']['time'],
            }
        else:
            return {
                "amount_burned": 0,
                "balance_due": 0,
                "balance_paid": 0,
                "last_withdrawal": 0,
                "last_burn": 0,
            }

    def get_merchant_portfolio(self, data):

        if isinstance(data, dict):
            self.checks = True
        self.checks = False

        data = data.get('result', {}).get('Ok', {}).get('data', {})
        res = data['Ok']

        if res:
            timestamp = res['last_conversion']
            dt = datetime.datetime.fromtimestamp(timestamp / 1000)
            now = datetime.datetime.now()
            days_difference = (now - dt).days
            redeemed_usdt = numbers.DecimalTruncation(2).format_usdt((res['green_points'] + res['relationship_factors'][
                0] + res['relationship_factors'][1]) * 0.0005 / 100 * days_difference)

            return {
                "green_points": numbers.DecimalTruncation(2).format_usdt(res['green_points']),
                "relationship_green_points": numbers.DecimalTruncation(2).format_usdt(res['green_points'] * 0.0005),
                "relationship_red_points": numbers.DecimalTruncation(2).format_usdt(
                    res['relationship_factors'][0] + res['relationship_factors'][1]),
                "last_conversion": res['last_conversion'],
                "redeemed_usdt": redeemed_usdt,
                "redeemed_d9": numbers.DecimalTruncation(2).format_d9(res['redeemed_d9']),
                "created_at": res['created_at'],
            }
        else:
            return {
                "green_points": 0,
                # "relationship_factors": list(res['relationship_factors']),
                "red_points": 0,
                "last_conversion": 0,
                "redeemed_usdt": 0,
                "redeemed_d9": 0,
                "created_at": 0,
            }


extractor = JSONExtractor()
