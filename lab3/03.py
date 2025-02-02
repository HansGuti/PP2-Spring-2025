def solve(numheads, numlegs):
    for rabbits in range(numheads + 1):
        chickens = numheads - rabbits
        if (2 * chickens + 4 * rabbits) == numlegs:
            return chickens, rabbits
chickens, rabbits = solve(35, 94)
print(f'chickens: {chickens}\nrabbits: {rabbits}')
