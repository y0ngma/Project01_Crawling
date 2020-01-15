# 리눅스에서만 가능함. 따라서 다음을 설치
# pip install apscheduler
# https://apscheduler.readthedocs.io/en/v2.1.2/cronschedule.html
from apscheduler.schedulers.blocking import BlockingScheduler
import time

def exec_interval(): # 일정시간 간격으로 수행
    print("hello world")

def exec_cron():
    strf = time.strftime('%c', time.localtime(time.time()))
    print('cron', strf)

sched   = BlockingScheduler()
# 5초 간격으로 exec_interval()함수 호출
sched.add_job(exec_interval, 'interval', seconds=5)

# 예약 방식(매시간 10초, 30일경우 구동)
sched.add_job(exec_cron, 'cron', minute="*", second="10, 30")
sched.start()


