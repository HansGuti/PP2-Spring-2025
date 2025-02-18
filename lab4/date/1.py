import datetime

x = datetime.datetime.now()
res = x - datetime.timedelta(days=5)
print(res.strftime('%Y-%B-%d'))