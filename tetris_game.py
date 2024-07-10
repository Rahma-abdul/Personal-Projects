import random
import os
import time

# Define the dimensions of the board
BOARD_WIDTH = 10
BOARD_HEIGHT = 20

# Define the shapes of the Tetris pieces
TETROMINOS = [
      [[0, 1], [1, 1], [1, 0], [2, 0]],  
      [[0, 2], [1, 0], [1, 1], [1, 2]],  
      [[0, 0], [1, 0], [1, 1], [2, 1]],  
      [[1, 0], [1, 1], [1, 2], [2, 0]],  
      [[0, 0], [0, 1], [1, 1], [1, 2]],  
      [[1, 0], [1, 1], [2, 1], [2, 2]],  
      [[0, 1], [1, 1], [1, 2], [2, 1]],
      [[1, 1, 1, 1]],
      [[1, 1], [1, 1]],
      [[1, 1, 0], [0, 1, 1]],
      [[0, 1, 1], [1, 1, 0]],
      [[1, 1, 1], [0, 1, 0]],
      [[1, 1, 1], [1, 0, 0]],
      [[1, 1, 1], [0, 0, 1]]
]
# Initialize the board
def Board():
    return [[0] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]

# Print the board to the console
def PrintBoard(board):
    os.system('cls')  # Use 'cls' for Windows
    print("~~~~~~~~GAME ON~~~~~~~~\n")
    for row in board:
        print(''.join(str(cell) if cell != 0 else '-' for cell in row))
    print("\n")

# Check if the piece can be placed on the board
def EmptySpot(board, shape, offset):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                if x + off_x < 0 or x + off_x >= BOARD_WIDTH or y + off_y >= BOARD_HEIGHT or board[y + off_y][x + off_x]:
                    return False
    return True

# Add the piece to the board
def FitPiece(board, shape, offset):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                board[y + off_y][x + off_x] = 7

# Remove completed lines
def WinLine(board):
    new_board = [row for row in board if any(cell == 0 for cell in row)]
    while len(new_board) < BOARD_HEIGHT:
        new_board.insert(0, [0] * BOARD_WIDTH)
    return new_board

def PickPosition(board, shape):
    best_score = None
    best_position = None

    for rotation in range(4):
        rotated_shape = RotatePiece(shape, rotation)
        for x in range(BOARD_WIDTH - len(rotated_shape[0]) + 1):
            y = 0
            while EmptySpot(board, rotated_shape, (x, y)):
                y += 1
            y -= 1
            if y < 0:
                continue
            new_board = [row[:] for row in board]
            FitPiece(new_board, rotated_shape, (x, y))
            new_board = WinLine(new_board)
            score = Score(new_board)
            if best_score is None or score < best_score:
                best_score = score
                best_position = (x, y, rotation)

    return best_position

# Rotate the piece
def RotatePiece(shape, rotation):
    for _ in range(rotation):
        shape = [list(row) for row in zip(*shape[::-1])]
    return shape

# Evaluate the board (heuristic)
def Score(board):
    return sum(sum(row) for row in board)


# The game loop
def GameOn():
    board = Board()
    score = 0

    while True:
        shape = random.choice(TETROMINOS)
        position = PickPosition(board, shape)
        if position is None:
            break
        x, y, rotation = position
        rotated_shape = RotatePiece(shape, rotation)
        FitPiece(board, rotated_shape, (x, y))
        board = WinLine(board)
        PrintBoard(board)
        score += 1
        time.sleep(1)

    print("Game Over. Your score is:", score)

if __name__ == "__main__":
    GameOn()
