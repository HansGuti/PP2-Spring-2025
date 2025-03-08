import time

def root_after_msec(num, msec = 0):
    time.sleep(msec / 1000)
    return num ** .5


print('Sample Input:')
num_for_sqrt = int(input())
msec = int(input())
print('Sample Output:')
print(f'Square root of {num_for_sqrt} after {msec} is {root_after_msec(num_for_sqrt, msec)}')