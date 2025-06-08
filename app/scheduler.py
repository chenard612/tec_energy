from apscheduler.schedulers.background import BackgroundScheduler
from app.api import query_csv

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(query_csv, 'interval', hours=6)
    scheduler.start()