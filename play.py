import numpy as np
ROW_COUNT = 6
COLUMN_COUNT = 7
board = np.zeros((ROW_COUNT, COLUMN_COUNT))
data = [5] * 7
t = 1


def check():
    vert = 0
    horiz = 0
    # Check horizontal
    for r in board:
        for i in r:
            if i == t:
                horiz += 1
            else:
                horiz = 0
            if horiz == 4:
                return True

    # Check vertical
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == t:
                vert += 1
            else:
                vert = 0
            if vert == 4:
                return True

    # Check diagonal
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == t and board[r - 1][c - 1] == t and board[r - 2][c - 2] == t and board[r - 3][c - 3] == t:
                return True

    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == t and board[r - 1][c + 1] == t and board[r - 2][c + 2] == t and board[r - 3][c + 3] == t:
                return True


game_over = False
while not game_over:
    print(board)
    m = int(input("column: ")) - 1
    while board[data[m]][m] != 0:
        data[m] -= 1
    if board[data[m]][m] == 0:
        board[data[m]][m] = t
    if check():
        print(board)
        print(f"connect 4 for player {t}")
        game_over = True

    t += 1 if t == 1 else -1
