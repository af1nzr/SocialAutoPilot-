import schedule
import time

class Scheduler:
    def __init__(self):
        self.jobs = []

    def add_task(self, func, time_interval):
        job = schedule.every(time_interval).minutes.do(func)
        self.jobs.append(job)

    def run(self):
        while True:
            schedule.run_pending()
            time.sleep(1)
