def sphere_volume(r):
    return round((4 / 3) * 3.14 * r ** 3, 2)
r = int(input('Radius: '))
print(sphere_volume(r))