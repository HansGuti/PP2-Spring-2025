import datetime

x = datetime.datetime.now()
y = x - datetime.timedelta(days=1)
z = x + datetime.timedelta(days=1)

print(f"Today: {x.strftime('%Y-%B-%d-%A')}")
print(f"Yesterday: {y.strftime('%Y-%B-%d-%A')}")
print(f"Tomorrow: {z.strftime('%Y-%B-%d-%A')}")
 