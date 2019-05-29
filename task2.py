import datetime

dt_now = datetime.datetime.now()

print('сегодня ', dt_now)

delta = datetime.timedelta(days=1)
print('вчера ', dt_now - delta)

delta = datetime.timedelta(days=30) # как отнять ровно месяц не знаю
print('не вчера ', dt_now - delta)

date_string = '01/01/17 12:10:03.234567'
date_dt = datetime.datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
print(date_dt)