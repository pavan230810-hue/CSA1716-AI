rooms = {'A': 1, 'B': 1}
position = 'A'

while 1 in rooms.values():
    if rooms[position] == 1:
        print("Cleaning room", position)
        rooms[position] = 0
    else:
        position = 'B' if position == 'A' else 'A'

print("All rooms are clean")
