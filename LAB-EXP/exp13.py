def minimax(depth, index, maximizing, values):
    if depth == 2:
        return values[index]

    if maximizing:
        return max(
            minimax(depth + 1, index * 2, False, values),
            minimax(depth + 1, index * 2 + 1, False, values)
        )
    else:
        return min(
            minimax(depth + 1, index * 2, True, values),
            minimax(depth + 1, index * 2 + 1, True, values)
        )

values = [3, 5, 2, 9]
print("Best value:", minimax(0, 0, True, values))
