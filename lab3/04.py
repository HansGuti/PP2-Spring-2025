import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    prime_numbers = []
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

numbers_str = input("Enter numbers separated by spaces: ").split()  
numbers = []  

for num in numbers_str:  
    numbers.append(int(num))

prime_numbers = filter_prime(numbers)

print("Prime numbers:", prime_numbers)
