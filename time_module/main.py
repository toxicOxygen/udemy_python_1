import time

t = time.localtime()
time_now = time.time()
week_from_now = time_now + (3600 * 24 * 7)
week_date = time.localtime(week_from_now)
print(week_date)