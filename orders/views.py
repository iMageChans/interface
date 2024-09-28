# merchant/views.py

import uuid
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import D9TransferSerializer
from .models import Order
from .tasks import process_d9_transfer_order

class D9TransactionView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = D9TransferSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # 从请求中获取密钥对，但不保存
        keypair = request.data.get('keypair')
        path = request.data.get('path')
        if not keypair:
            return Response({'error': 'Keypair is required'}, status=status.HTTP_400_BAD_REQUEST)

        # 生成订单 ID
        order_id = str(uuid.uuid4())

        # 创建订单记录
        order = Order.objects.create(
            order_id=order_id,
            operation='d9_transfer',
            params=serializer.validated_data,
            status='pending'
        )

        # 触发后台任务，处理订单
        process_d9_transfer_order.delay(order_id, keypair, path)

        return Response({
            'message': 'Order has been created and is being processed',
            'order_id': order_id
        }, status=status.HTTP_202_ACCEPTED)

# class ExecuteD9TransactionView(BaseOrderView):
#     serializer_class = serializers.ExecuteD9TransactionSerializer
#     operation = 'execute_d9_transaction'
