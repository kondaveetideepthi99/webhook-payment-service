**Tech stack:**
Django rest framework
Celery,Redis
MySQL
Render
Aiven(MySQL)
Upstash(Reddis)

**Install Dependencies:**
pip install -r requirements.txt

**Follow the order to run terminals:**
1.Start Redis:
redis-server
2.Run Django server:
python manage.py runserver
3.Run Celery
celery -A webhook_payment_service worker --loglevel=info --pool=solo

**The live API**:
https://webhook-payment-service.onrender.com

**Check with endpoints**
**with celery worker working in the background, Test in postman**:

**Method**:POST

**URL**:https://webhook-payment-service.onrender.com/v1/webhooks/transactions
**Body(JSON)**:
{
 "transaction_id": "txn_1",
 "source_account": "acc_user_789",
 "destination_account": "acc_merchant_456",
 "amount": 1500,
 "currency": "INR"
}

**After 30secs, check transaction status:**
**Method**:GET
**URL:** https://webhook-payment-service.onrender.com/v1/transactions/txn_1

As celery woker is paid version in Render, you can check locally using the same dependencies:
**Start Redis**:
redis-server
**Run Django Server:**
python manage.py runserver
**Run celery worker:**
celery -A webhook_payment_service worker --loglevel=info --pool=solo

**Method**:POST

**URL**:http://127.0.0.1:8000/v1/webhooks/transactions
**Body(JSON)**:
{
 "transaction_id": "txn_1",
 "source_account": "acc_user_789",
 "destination_account": "acc_merchant_456",
 "amount": 1500,
 "currency": "INR"
}

**After 30secs, check transaction status:**
**Method**:GET
**URL:** http://127.0.0.1:8000/v1/transactions/txn_1

The transactions will be processed asynchronously in the background
