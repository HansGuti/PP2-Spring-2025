def square_of_numbers(N):
    count = 1
    cnt = 1
    
    while count <= N:
        yield count
        cnt += 1
        count = cnt ** 2
for i in square_of_numbers(8): 
    print(i)