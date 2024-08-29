import requests
from utils.numbers import DecimalTruncation
from usdt.models import CurrencyProfile


def update_or_created_currency_profile():
    supported_currencies_url = "https://api.coingecko.com/api/v3/simple/supported_vs_currencies"
    response = requests.get(supported_currencies_url)

    if response.status_code == 200:
        supported_currencies = response.json()
    else:
        print("Failed to retrieve supported currencies")
        supported_currencies = []

    if supported_currencies:
        vs_currencies = ','.join(supported_currencies)

        usdt_price_url = f"https://api.coingecko.com/api/v3/simple/price?ids=tether&vs_currencies={vs_currencies}"
        response = requests.get(usdt_price_url)

        if response.status_code == 200:
            usdt_prices = response.json().get('tether', {})
            for currency in usdt_prices:
                data = {
                    "name": currency,
                    "price": DecimalTruncation(8).format(usdt_prices[currency]),
                }
                CurrencyProfile.objects.update_or_create(
                    name=currency,
                    defaults=data
                )

        else:
            print("Failed to retrieve USDT prices")
    else:
        print("No supported currencies available")