from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Transaction
from .serializers import WebhookSerializer, TransactionSerializer

# Health Check Endpoint
class HealthCheckView(APIView):
    def get(self, request):
        return Response({
            "status": "HEALTHY",
            "current_time": timezone.now().isoformat()
        })


# Webhook Receiver
class WebhookTransactionView(APIView):
    def post(self, request):
        serializer = WebhookSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            # Create or get the transaction (idempotent)
            obj, created = Transaction.objects.get_or_create(
                transaction_id=data["transaction_id"],
                defaults=data
            )


            if created:
                from .tasks import process_transaction
                print(f"Queuing task for: {obj.transaction_id}")
                process_transaction.delay(obj.transaction_id)
            else:
                print(f" Transaction {obj.transaction_id} already exists — skipping reprocess")

            # Always respond quickly
            return Response({"message": "Accepted OK"}, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Get Transaction Status
class TransactionStatusView(APIView):
    def get(self, request, transaction_id):
        try:
            transaction = Transaction.objects.get(transaction_id=transaction_id)
            serializer = TransactionSerializer(transaction)
            return Response(serializer.data)
        except Transaction.DoesNotExist:
            return Response({"error": "Transaction not found"}, status=404)
