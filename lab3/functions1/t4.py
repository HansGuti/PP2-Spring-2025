def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    res = []
    for i in range(0, len(numbers)):
        num = numbers[i]
        if is_prime(num):
            res.append(num)
    return res

user_input = input('Enter numbers separated by spaces: ')

nums_list = []
split_input = user_input.split()

for i in range(0, len(split_input)):
    x = split_input[i]
    number = int(x)
    nums_list.append(number)

primes = filter_prime(nums_list)
print('Prime numbers:', primes)