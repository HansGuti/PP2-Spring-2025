def histogram(x):
    return lambda a : '*' * x
x = int(input())
print(histogram(*x))