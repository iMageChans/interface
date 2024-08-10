def format_number(value, precision=12):
    if isinstance(value, str):
        value = float(value)

    result = value / 10 ** precision

    if result.is_integer():
        return int(result)
    else:
        return result


def to_number(value, precision=12):
    if isinstance(value, str):
        value = float(value)

    result = value * 10 ** precision

    if result.is_integer():
        return int(result)
    else:
        return result


def format_d9(number):
    return format_number(number)


def format_usdt(number):
    return format_number(number, 2)


def to_d9(number):
    return to_number(number)


def to_usdt(number):
    return to_number(number, 2)


def get_return_percent(total_amount_burned):
    first_threshold_amount = 200_000_000
    percentage = 0.008

    if total_amount_burned <= first_threshold_amount:
        return percentage

    excess_amount = total_amount_burned - first_threshold_amount
    reductions = excess_amount // 100_000_000 + 1
    divided_percent_by = 2 ** reductions

    return percentage / divided_percent_by


class DecimalTruncation:
    def __init__(self, precision):
        self.precision = precision

    def truncate(self, number):
        """
        :param number: Decimals that need to be truncated
        :return: Captured numbers
        """
        if not isinstance(number, (float, int)):
            raise ValueError("The input must be a floating-point number or an integer")

        number_str = f"{number:.{self.precision + 10}f}"
        integer_part, decimal_part = number_str.split('.')
        truncated_decimal_part = decimal_part[:self.precision]

        if len(truncated_decimal_part) < 2:
            truncated_decimal_part = truncated_decimal_part.ljust(2, '0')

        truncated_number_str = f"{integer_part}.{truncated_decimal_part}"
        return truncated_number_str

    def format_d9(self, number):
        return self.truncate(format_number(number))

    def format_usdt(self, number):
        return self.truncate(format_number(number, 2))

    def format_point(self, number):
        return self.truncate(format_number(number, 3))

    def format(self, number):
        return self.truncate(format_number(number, 0))
