from decimal import Decimal, ROUND_DOWN
from typing import Union


def format_number(value: Union[str, float, int], precision: int = 12) -> Decimal:
    """
    Format the number by dividing by 10^precision.

    :param value: The number to format.
    :param precision: The precision factor.
    :return: Formatted Decimal number.
    :raises ValueError: If the input value is invalid.
    """
    try:
        decimal_value = Decimal(str(value))
        return decimal_value / (Decimal(10) ** precision)
    except (ValueError, ArithmeticError) as e:
        raise ValueError(f"Failed to format number: {e}") from e


def to_number(value: Union[str, float, int], precision: int = 12) -> int:
    """
    Convert the number by multiplying by 10^precision and ensure it is an unsigned integer.

    :param value: The number to convert.
    :param precision: The precision factor.
    :return: Converted unsigned integer.
    :raises ValueError: If the result is negative or not an integer.
    """
    try:
        decimal_value = Decimal(str(value)) * (Decimal(10) ** precision)
        # Ensure the result is an integer
        if not decimal_value == decimal_value.to_integral_value():
            raise ValueError("The converted number is not an integer.")
        int_value = int(decimal_value)
        if int_value < 0:
            raise ValueError("The converted number is negative.")
        return int_value
    except (ValueError, ArithmeticError) as e:
        raise ValueError(f"Failed to convert number: {e}") from e


def format_d9(number: Union[str, float, int, Decimal]) -> Decimal:
    """
    Format a D9 token value by dividing by 10^12.

    :param number: The number to format.
    :return: Formatted Decimal number.
    """
    return format_number(number)


def format_usdt(number: Union[str, float, int, Decimal]) -> Decimal:
    """
    Format a USDT token value by dividing by 10^2.

    :param number: The number to format.
    :return: Formatted Decimal number.
    """
    return format_number(number, 2)


def to_d9(number: Union[str, float, int, Decimal]) -> int:
    """
    Convert a D9 token value by multiplying by 10^12 and return as an unsigned integer.

    :param number: The number to convert.
    :return: Converted unsigned integer.
    """
    return to_number(number)


def to_usdt(number: Union[str, float, int, Decimal]) -> int:
    """
    Convert a USDT token value by multiplying by 10^2 and return as an unsigned integer.

    :param number: The number to convert.
    :return: Converted unsigned integer.
    """
    return to_number(number, 2)
