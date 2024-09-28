# wallets/views.py
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from wallets.models import Wallet
from wallets.serializers import D9BalancesSerializer, USDTBalancesSerializer , RetrieveWalletSerializer
from wallets.service.d9_balances import D9Balances
from utils.numbers import format_d9, format_usdt
from utils.keystone import check_keypair
from utils.JSONExtractor import JSONExtractor
from wallets.service.usdt_balances import USDTBalances


class BaseView(APIView):
    serializer_class = None
    operation = None
    instance = None

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        method = getattr(self.instance, self.operation, None)
        if not method:
            raise ValueError(f'Unsupported operation: {self.operation}')

        result = method(**serializer.validated_data)
        return Response(result.value_serialized, status=status.HTTP_200_OK)


class D9BalancesView(BaseView):
    serializer_class = D9BalancesSerializer
    operation = 'd9_balances'
    instance = D9Balances()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        params = serializer.validated_data.copy()

        method = getattr(self.instance, self.operation, None)
        if not method:
            raise ValueError(f'Unsupported operation: {self.operation}')

        result = method(**params)
        responses = result.value_serialized

        wallet_data = {
            'address': f'Dn{params["to_address"]}',
            'd9': format_d9(responses['data']['free']),
        }

        wallet, created = Wallet.objects.update_or_create(
            address=f'Dn{params["to_address"]}',
            defaults={
                'd9': format_d9(responses['data']['free'])
            }
        )
        wallet_serializer = RetrieveWalletSerializer(wallet)
        if created:
            return Response(wallet_serializer.data, status=status.HTTP_201_CREATED)
        return Response(wallet_serializer.data, status=status.HTTP_200_OK)

class USDTBalancesView(BaseView):
    serializer_class = USDTBalancesSerializer
    operation = 'usdt_balances'

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        params = serializer.validated_data.copy()

        keypair = request.data.get('keypair')
        if not keypair:
            return Response({'error': 'keypair is required'}, status=status.HTTP_400_BAD_REQUEST)
        instance = USDTBalances(keypair=check_keypair(keypair=keypair))

        method = getattr(instance, self.operation, None)
        if not method:
            raise ValueError(f'Unsupported operation: {self.operation}')

        result = method(**params)
        responses = result.value_serialized
        usdt_balance = JSONExtractor().get_data_or_err(responses)

        wallet_data = {
            'address': f'Dn{params["to_address"]}',
            'usdt': format_usdt(usdt_balance),
        }

        wallet, created = Wallet.objects.update_or_create(
            address=f'Dn{params["to_address"]}',
            defaults={
                'usdt': format_usdt(usdt_balance)
            }
        )
        wallet_serializer = RetrieveWalletSerializer(wallet)
        if created:
            return Response(wallet_serializer.data, status=status.HTTP_201_CREATED)
        return Response(wallet_serializer.data, status=status.HTTP_200_OK)


class WalletsView(BaseView):
    def get(self, request, *args, **kwargs):
        address = request.query_params.get('to_address', None)
        if not address:
            return Response({"detail": "to_address query parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            wallet = Wallet.objects.get(address=address)
        except Wallet.DoesNotExist:
            raise NotFound(detail="Wallet not found.")

        wallet_serializer = RetrieveWalletSerializer(wallet)
        return Response(wallet_serializer.data, status=status.HTTP_200_OK)

