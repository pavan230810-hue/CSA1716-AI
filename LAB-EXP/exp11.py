colors = ['Red', 'Green', 'Blue']

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}

result = {}

def solve():
    for place in graph:
        for color in colors:
            valid = True

            for neighbor in graph[place]:
                if result.get(neighbor) == color:
                    valid = False

            if valid:
                result[place] = color
                break

    return result

print(solve())
