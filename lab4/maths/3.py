import math

num_of_sides = int(input('Input number of sides: '))
length_of_side = int(input('Input the length of a side: '))
area = math.floor((num_of_sides * pow(length_of_side, 2)) / (4 * math.tan(math.pi / num_of_sides)))
print(f'The area of the polygon is: {area}')