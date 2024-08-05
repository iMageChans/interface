from decimal import Decimal

from amm.models import TokenMarketInformation
from utils import numbers


def rate(balance_0, balance_1, amount_0):
    try:
        # Convert input values to Decimal type to ensure high-precision calculations
        fixed_balance_0 = Decimal(balance_0)
        fixed_balance_1 = Decimal(balance_1)
        fixed_amount_0 = Decimal(amount_0)

        # Calculate the constant product k
        fixed_curve_k = fixed_balance_0 * fixed_balance_1

        # Calculate the new balance_0
        new_balance_0 = fixed_balance_0 + fixed_amount_0

        # Calculate the new balance_1 and throw an exception if divided by zero
        new_balance_1 = fixed_curve_k / new_balance_0

        # Calculate the reduced amount_1
        amount_1 = fixed_balance_1 - new_balance_1

        # Return result, convert back to float type
        return float(amount_1)
    except Exception as err:
        raise ValueError("Division by zero occurred", err)


def get_currency_rate_amount(from_currency, to_currency, amount):
    first_currency_reserve = TokenMarketInformation.objects.order_by("-created_at").first()
    usdt = numbers.format_number(int(first_currency_reserve.usdt_token), 2)
    d9 = numbers.format_number(int(first_currency_reserve.d9_token))
    if from_currency == "USDT" and to_currency == "D9":
        return rate(usdt, d9, amount)
    elif from_currency == "D9" and to_currency == "USDT":
        return rate(d9, usdt, amount)
    else:
        raise ValueError("Currency must be either USDT or D9")