from itertools import permutations

cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cities = [1, 2, 3]
minimum = 9999

for p in permutations(cities):
    route = (0,) + p + (0,)
    total = 0

    for i in range(len(route) - 1):
        total += cost[route[i]][route[i+1]]

    if total < minimum:
        minimum = total
        best = route

print("Best route:", best)
print("Minimum cost:", minimum)
