import schedule
import time 
import datetime

def doSchedule():
    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M:%S")
    print("success post : " + " at:" + time)

schedule.every().minutes.do(doSchedule)

while True:
    schedule.run_pending()
    time.sleep(1)
