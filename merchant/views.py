# merchant/views.py

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from merchant import serializers
from merchant.models import TransactionRecord
from merchant.tasks import execute_transaction

class BaseView(APIView):
    serializer_class = None
    operation = None  # 子类需要定义

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # 从请求中获取密钥对，但不保存
        keypair = request.data.get('keypair')
        if not keypair:
            return Response({'error': 'Keypair is required'}, status=status.HTTP_400_BAD_REQUEST)

        # 创建交易记录
        transaction = TransactionRecord.objects.create(
            user=request.user,
            operation=self.operation,
            params=serializer.validated_data,
            status='pending'
        )

        # 将任务加入后台队列
        execute_transaction.delay(transaction.id, keypair)

        return Response({
            'message': 'Transaction is being processed',
            'transaction_id': transaction.id
        }, status=status.HTTP_202_ACCEPTED)

class SubscribeView(BaseView):
    serializer_class = serializers.SubscribeSerializer
    operation = 'subscribe'

class RedeemD9View(BaseView):
    serializer_class = serializers.RedeemD9Serializer
    operation = 'redeem_d9'

class GivePointsD9View(BaseView):
    serializer_class = serializers.GivePointsD9Serializer
    operation = 'give_points_d9'

class GivePointsUSDTView(BaseView):
    serializer_class = serializers.GivePointsUSDTSerializer
    operation = 'give_points_usdt'

class SendUSDTPaymentToMerchantView(BaseView):
    serializer_class = serializers.USDTPaymentSerializer
    operation = 'send_usdt_payment_to_merchant'

class SendD9PaymentToMerchantView(BaseView):
    serializer_class = serializers.D9PaymentSerializer
    operation = 'send_d9_payment_to_merchant'
