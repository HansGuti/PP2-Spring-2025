import datetime

x = datetime.datetime.now()
res = x.replace(microsecond=0)
print(f"Datetime without microseconds: {res}")