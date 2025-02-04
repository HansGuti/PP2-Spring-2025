def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        total_legs = 4 * rabbits + 2 * chickens
        if total_legs == numlegs:
            return chickens, rabbits
    return None

heads = int(input('Type in number of heads: '))
legs = int(input('Type in number of legs: '))
result = solve(heads, legs)

if result:
    chickens, rabbits = result
    print('Chickens:', chickens, 'Rabbits:', rabbits)
else:
    print('There is no solution!')