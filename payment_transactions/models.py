from django.db import models

class Transaction(models.Model):
    STATUS_CHOICES = [
        ("PROCESSING", "Processing"),
        ("PROCESSED", "Processed"),
        ("FAILED", "Failed"),
    ]

    transaction_id = models.CharField(max_length=128, unique=True)
    source_account = models.CharField(max_length=128)
    destination_account = models.CharField(max_length=128)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PROCESSING")
    created_at = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(null=True, blank=True)
    last_error = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.transaction_id} - {self.status}"
