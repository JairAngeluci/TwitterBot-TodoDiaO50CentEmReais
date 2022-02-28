from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler(timezone="america/sao_paulo")

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=12)
def scheduled_job():
    print('Exec 1000...')
    exec(open('TodoDiaO50CentEmReais.py').read())

sched.start()