from decimal import Decimal, ROUND_DOWN
from typing import Union
from amm.models import TokenMarketInformation
from utils.numbers import format_number
import logging

logger = logging.getLogger(__name__)

def rate(balance_0: Union[str, float, int], balance_1: Union[str, float, int], amount_0: Union[str, float, int]) -> float:
    fixed_balance_0 = Decimal(balance_0)
    fixed_balance_1 = Decimal(balance_1)
    fixed_amount_0 = Decimal(amount_0)

    new_balance_0 = fixed_balance_0 + fixed_amount_0
    if new_balance_0 == 0:
        logger.error("New balance_0 results in division by zero.")
        raise ZeroDivisionError("New balance_0 results in division by zero.")

    fixed_curve_k = fixed_balance_0 * fixed_balance_1
    new_balance_1 = fixed_curve_k / new_balance_0
    amount_1 = fixed_balance_1 - new_balance_1

    return float(amount_1)

def get_currency_rate_amount(from_currency: str, to_currency: str, amount: Union[str, float, int]) -> float:
    first_currency_reserve = TokenMarketInformation.objects.order_by("-created_at").first()
    if not first_currency_reserve:
        logger.error("No currency reserve data available.")
        raise ValueError("No currency reserve data available.")

    usdt = format_number(int(first_currency_reserve.usdt_token), 2)
    d9 = format_number(int(first_currency_reserve.d9_token), 12)  # Assuming default precision

    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    if from_currency == "USDT" and to_currency == "D9":
        return rate(usdt, d9, amount)
    elif from_currency == "D9" and to_currency == "USDT":
        return rate(d9, usdt, amount)
    else:
        logger.error("Unsupported currency conversion attempted.")
        raise ValueError("Currency must be either USDT or D9")

def get_return_percent(total_amount_burned: int) -> float:
    FIRST_THRESHOLD = 200_000_000
    BASE_PERCENTAGE = 0.008

    if total_amount_burned <= FIRST_THRESHOLD:
        return BASE_PERCENTAGE

    excess = total_amount_burned - FIRST_THRESHOLD
    reductions = (excess // 100_000_000) + 1
    return BASE_PERCENTAGE / (2 ** reductions)

class DecimalTruncation:
    def __init__(self, precision: int):
        self.precision = precision

    def truncate(self, number: Union[str, float, int, Decimal]) -> str:
        if not isinstance(number, (float, int, str, Decimal)):
            raise ValueError("The input must be a number or a numeric string.")

        decimal_number = Decimal(str(number))
        quantize_str = f'1.{"0" * self.precision}'
        truncated = decimal_number.quantize(Decimal(quantize_str), rounding=ROUND_DOWN)
        return format(truncated, 'f')

    def format_d9(self, number: Union[str, float, int, Decimal]) -> str:
        return self.truncate(format_number(number))

    def format_usdt(self, number: Union[str, float, int, Decimal]) -> str:
        return self.truncate(format_number(number, 2))

    def format_point(self, number: Union[str, float, int, Decimal]) -> str:
        return self.truncate(format_number(number, 3))

    def format(self, number: Union[str, float, int, Decimal]) -> str:
        return self.truncate(format_number(number, 0))
