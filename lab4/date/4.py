import datetime

x = datetime.datetime(2025, 1, 17)
y = datetime.datetime(2025, 2, 2)
diff = abs((x - y).total_seconds())

print(f'Difference of two dates in seconds: {diff}')
