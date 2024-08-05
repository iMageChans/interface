from amm.models import *
from utils import numbers


def update_or_created_token_market_information(validated_data):
    token_market_information = TokenMarketInformation.objects.order_by("-created_at").first()
    if (token_market_information
            and token_market_information.d9_token == str(validated_data['d9'])
            and token_market_information.usdt_token == str(validated_data['usdt'])):
        return token_market_information
    else:
        data = {
            'd9_token': validated_data['d9'],
            'usdt_token': validated_data['usdt'],
        }

        data.update({"usdt_rate":
                         float(numbers.DecimalTruncation(4).format_usdt(validated_data['usdt'])) /
                         float(numbers.DecimalTruncation(4).format_d9(validated_data['d9']))
                     })

        data.update({"d9_rate":
                         float(numbers.DecimalTruncation(4).format_d9(validated_data['d9'])) /
                         float(numbers.DecimalTruncation(4).format_usdt(validated_data['usdt']))
                     })

        token_market_information = TokenMarketInformation.objects.create(**data)
        return token_market_information
