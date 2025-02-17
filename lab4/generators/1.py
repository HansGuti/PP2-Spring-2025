def square_of_numbers(N):
    for i in range(1, N + 1):
        yield i ** 2

    
N = int(input('Enter: '))

for x in square_of_numbers(N):
    print(x)