from datetime import datetime

from schedule import every, repeat, run_pending


@repeat(every(20).seconds)
def task_for_seconds():
    now = datetime.now()
    print("This task runs every 20 seconds! ({})".format(now.strftime("%d/%m/%Y %H:%M:%S")))


@repeat(every().minutes)
def task_for_minutes():
    now = datetime.now()
    print("This task runs every minute! ({})".format(now.strftime("%d/%m/%Y %H:%M:%S")))


@repeat(every().minute.at(":10"))
def task_for_minutes_at_ten():
    now = datetime.now()
    print("This task runs every minute at 10 secs! ({})".format(now.strftime("%d/%m/%Y %H:%M:%S")))


@repeat(every(2).hours)
def task_for_hours():
    now = datetime.now()
    print("This task runs every 2 hours! ({})".format(now.strftime("%d/%m/%Y %H:%M:%S")))


@repeat(every(5).days)
def task_for_days():
    now = datetime.now()
    print("This task runs every 5 days! ({})".format(now.strftime("%d/%m/%Y %H:%M:%S")))


now = datetime.now()
print("Script starting at {}".format(now.strftime("%d/%m/%Y %H:%M:%S")))
# schedule all tasks
while True:
    run_pending()
