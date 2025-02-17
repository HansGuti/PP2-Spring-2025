def even_nums(n):
    while True:
        yield n


n = int(input('Type in a number: '))
for i in range(0, n + 1):
    if i % 2 == 0:
        print(f'{i},')
