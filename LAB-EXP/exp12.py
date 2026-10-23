board = [' '] * 9

def show():
    print(board[0], '|', board[1], '|', board[2])
    print('--+---+--')
    print(board[3], '|', board[4], '|', board[5])
    print('--+---+--')
    print(board[6], '|', board[7], '|', board[8])

player = 'X'

for i in range(9):
    show()
    pos = int(input("Enter position (1-9): ")) - 1

    if pos < 0 or pos > 8 or board[pos] != ' ':
        print("Invalid position")
        continue

    board[pos] = player

    if (board[0] == board[1] == board[2] != ' ' or
        board[3] == board[4] == board[5] != ' ' or
        board[6] == board[7] == board[8] != ' ' or
        board[0] == board[3] == board[6] != ' ' or
        board[1] == board[4] == board[7] != ' ' or
        board[2] == board[5] == board[8] != ' ' or
        board[0] == board[4] == board[8] != ' ' or
        board[2] == board[4] == board[6] != ' '):
        show()
        print(player, "wins!")
        break

    player = 'O' if player == 'X' else 'X'
else:
    show()
    print("Game Over")
