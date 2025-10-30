from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"

class WebhookSerializer(serializers.Serializer):
    transaction_id = serializers.CharField()
    source_account = serializers.CharField()
    destination_account = serializers.CharField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    currency = serializers.CharField()
