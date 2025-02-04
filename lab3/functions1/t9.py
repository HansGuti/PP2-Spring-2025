import math

def sphere(r):
    V = (4/3) * math.pi * r ** 3
    return V
user_input = int(input('Enter a radius (r): '))
print(sphere(user_input))