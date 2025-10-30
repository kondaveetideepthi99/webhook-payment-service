from django.urls import path
from .views import HealthCheckView, WebhookTransactionView, TransactionStatusView

urlpatterns = [
    path('', HealthCheckView.as_view(), name='health'),
    path('v1/webhooks/transactions', WebhookTransactionView.as_view(), name='webhook'),
    path('v1/transactions/<str:transaction_id>', TransactionStatusView.as_view(), name='status'),
]
