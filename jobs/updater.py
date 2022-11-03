from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler

from .get_twitts import Get_twetts


def start():
    schedule = BackgroundScheduler()
    schedule.add_job(Get_twetts, 'interval', seconds= 600)
    schedule.start()





