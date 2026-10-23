import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('D', 1)],
    'D': [('G', 3)],
    'E': [('G', 2)],
    'G': []
}

h = {'A': 5, 'B': 4, 'C': 4, 'D': 2, 'E': 1, 'G': 0}

q = [(h['A'], 0, 'A', ['A'])]
visited = set()

while q:
    f, cost, node, path = heapq.heappop(q)

    if node == 'G':
        print("Path:", path)
        print("Cost:", cost)
        break

    if node in visited:
        continue
    visited.add(node)

    for next_node, weight in graph[node]:
        if next_node not in visited:
            new_cost = cost + weight
            heapq.heappush(q, (
                new_cost + h[next_node],
                new_cost,
                next_node,
                path + [next_node]
            ))
