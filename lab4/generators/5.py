def count_down_to_zero(n):
    for i in range(n, -1, -1):
        yield i


n = int(input('Enter a number: '))
for x in count_down_to_zero(n):
    print(x)