import logging
from celery import shared_task
from .models import Order
from service.d9.contracts import D9PalletsBalances
from utils.keystone import check_keypair, ValidAddress
from utils.JSONExtractor import JSONExtractor
from utils.numbers import to_d9

logger = logging.getLogger(__name__)

@shared_task
def process_d9_transfer_order(order_id, keypair_uri, path=None):
    logger.debug("Debugging: Task has started.")
    logger.info(f"Starting process_d9_transfer_order for Order ID: {order_id}")
    order = Order.objects.get(order_id=order_id)

    try:
        keypair = check_keypair(keypair=keypair_uri, path=path)
        instance = D9PalletsBalances()

        from_address = keypair.ss58_address
        balance = instance.get_balances(to_address=from_address)
        balance = JSONExtractor().get_balances_d9(balance)
        order.from_address = f'Dn{from_address}'
        order.save()

        required_amount = to_d9(order.params.get('amount'))
        logger.info('required_amount: %s', required_amount)
        logger.info('balance: %s', balance)
        if balance < required_amount:
            order.status = 'failed'
            order.error = 'Insufficient balance'
            order.save()
            return

        to_address = ValidAddress(order.params.get('to_address')).get_valid_address()
        d9_transfer = instance.d9_transfer(to_address=to_address, amount=required_amount)
        gas_limit = d9_transfer.gas_required
        print(gas_limit)

    except Exception as e:
        order.status = 'failed'
        order.error = str(e)
        order.save()