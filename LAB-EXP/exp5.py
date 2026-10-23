from collections import deque

q = deque([(3, 3, 1, [])])
visited = set()

while q:
    m, c, boat, path = q.popleft()

    if (m, c, boat) in visited:
        continue
    visited.add((m, c, boat))

    path = path + [(m, c, boat)]

    if m == 0 and c == 0:
        for s in path:
            print(s)
        break

    for x, y in [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]:
        if boat == 1:
            nm, nc, nb = m-x, c-y, 0
        else:
            nm, nc, nb = m+x, c+y, 1

        if 0 <= nm <= 3 and 0 <= nc <= 3:
            if (nm == 0 or nm >= nc) and (nm == 3 or 3-nm >= 3-nc):
                q.append((nm, nc, nb, path))
