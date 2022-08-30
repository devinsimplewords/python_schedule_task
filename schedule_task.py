from datetime import datetime

import schedule


def task_for_seconds():
    now = datetime.now()
    print("This task runs every 20 seconds! ({})".format(now.strftime("%d/%m/%Y %H:%M:%S")))


def task_for_minutes():
    now = datetime.now()
    print("This task runs every minute! ({})".format(now.strftime("%d/%m/%Y %H:%M:%S")))


def task_for_minutes_at_ten():
    now = datetime.now()
    print("This task runs every minute at 10 secs! ({})".format(now.strftime("%d/%m/%Y %H:%M:%S")))


def task_for_hours():
    now = datetime.now()
    print("This task runs every 2 hours! ({})".format(now.strftime("%d/%m/%Y %H:%M:%S")))


def task_for_days():
    now = datetime.now()
    print("This task runs every 5 days! ({})".format(now.strftime("%d/%m/%Y %H:%M:%S")))


# Run task every 20 seconds
schedule.every(20).seconds.do(task_for_seconds)
# Run task every minute
schedule.every().minutes.do(task_for_minutes)
# Run task every 2 hours
schedule.every(2).hours.do(task_for_hours)
# Run task every 5 days
schedule.every(5).days.do(task_for_days)
# Run task every minute at the 10rd second
schedule.every().minute.at(":10").do(task_for_minutes_at_ten)

now = datetime.now()
print("Script starting at {}".format(now.strftime("%d/%m/%Y %H:%M:%S")))
# schedule all tasks
while True:
    schedule.run_pending()
