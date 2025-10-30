Tech stack:
Django rest framework
Celery,Redis
MySQL
Render
Aiven(MySQL)
Upstash(Reddis)

Install Dependencies:
pip install -r requirements.txt

Follow the order to run terminals:
1.Start Redis:
redis-server
2.Run Django server:
python manage.py runserver
3.Run Celery
celery -A webhook_payment_service worker --loglevel=info --pool=solo
