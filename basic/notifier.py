import time
import os
from functools import partial
from win10toast import ToastNotifier
from apscheduler.schedulers.background import BackgroundScheduler


def notification(title="Alert", description="Test notification", duration=5):
    toaster = ToastNotifier()
    toaster.show_toast(title, description, duration=duration)


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    cron_notify = partial(notification, "Cron alert", "Hi, it's cron scheduler")
    interval_notify = partial(notification, "Interval alert", "Hi, it's interval scheduler")
    scheduler.add_job(cron_notify, "cron", id="cron_notify", hour=13, minute=38)
    scheduler.add_job(interval_notify, "interval", id="interval_notify", seconds=10)
    jobs = scheduler.get_jobs()
    scheduler.start()
    print("Press Ctrl+C to exit")

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
