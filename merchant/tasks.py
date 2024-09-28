# merchant/tasks.py

from celery import shared_task
from substrateinterface import Keypair
from merchant.models import TransactionRecord
from merchant.service.exec import Exec
from utils.keystone import check_keypair

@shared_task
def execute_transaction(transaction_id, keypair_uri):
    transaction = TransactionRecord.objects.get(id=transaction_id)
    try:
        params = transaction.params.copy()
        operation = transaction.operation

        keypair = check_keypair(keypair_uri)

        exec_instance = Exec(keypair=keypair)

        method = getattr(exec_instance, operation, None)
        if not method:
            raise ValueError(f'Unsupported operation: {operation}')

        result = method(**params)

        if result.is_success:
            transaction.status = 'success'
            transaction.result = {'data': result.value}
        else:
            transaction.status = 'failed'
            transaction.result = {'error': result.error_message}
        transaction.save()

    except Exception as e:
        transaction.status = 'failed'
        transaction.result = {'exception': str(e)}
        transaction.save()
