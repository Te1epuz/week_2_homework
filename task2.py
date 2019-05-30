import datetime

dt_now = datetime.datetime.now()

print('сегодня ', dt_now)

delta = datetime.timedelta(days=1)
print('вчера ', dt_now - delta)

# как отнять ровно месяц не придумал, поэтому списал
month = (dt_now.replace(day=1) - datetime.timedelta(days=1)).month
year = dt_now.year - (dt_now.month - 1 < 1)
day = min(dt_now.day, (dt_now.replace(day=1) - datetime.timedelta(days=1)).day)
print('месяц назад ', datetime.datetime(year,month,day).strftime('%Y.%m.%d'))


date_string = '01/01/17 12:10:03.234567'
date_dt = datetime.datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
print(date_dt)