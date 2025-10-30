import time
from celery import shared_task
from django.utils import timezone
from .models import Transaction


@shared_task(bind=True)
def process_transaction(self, transaction_id):
    try:
        txn = Transaction.objects.get(transaction_id=transaction_id)
        if txn.status == "PROCESSED":
            return f"{transaction_id} already processed"

        time.sleep(30)
        txn.status = "PROCESSED"
        txn.processed_at = timezone.now()
        txn.save()
        print(f" Transaction {transaction_id} processed successfully")
        return f"{transaction_id} processed"
    except Exception as e:
        txn.status = "FAILED"
        txn.last_error = str(e)
        txn.save()
        print(f" Transaction {transaction_id} failed: {e}")
        raise self.retry(exc=e, countdown=10, max_retries=3)

