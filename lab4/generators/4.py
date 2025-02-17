def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2


a = int(input('Enter the first number: '))
b = int(input('Enter the last number: '))
print(f'The square of numbers between {a} and {b} are:')
for x in squares(a, b):
    print(x)    