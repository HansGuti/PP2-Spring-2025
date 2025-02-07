def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

mylist = [1, 2, 3, 4, 5, 6, 7, 19, 31, 42]
print(list(filter(lambda x: is_prime(x), mylist)))