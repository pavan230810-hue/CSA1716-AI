from heapq import heappush, heappop

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def heuristic(state):
    return sum(state[i] != 0 and state[i] != goal[i]
               for i in range(9))

def solve():
    pq = []
    heappush(pq, (0, start, []))
    visited = set()

    while pq:
        cost, state, path = heappop(pq)

        if state in visited:
            continue
        visited.add(state)

        path = path + [state]

        if state == goal:
            for s in path:
                print(s[0:3])
                print(s[3:6])
                print(s[6:9])
                print()
            return

        zero = state.index(0)
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in moves:
            x, y = zero // 3 + dx, zero % 3 + dy

            if 0 <= x < 3 and 0 <= y < 3:
                new = list(state)
                pos = x * 3 + y
                new[zero], new[pos] = new[pos], new[zero]
                new = tuple(new)

                if new not in visited:
                    heappush(pq, (cost + 1 + heuristic(new),
                                  new, path))

solve()
