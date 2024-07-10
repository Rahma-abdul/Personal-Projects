# Self-Playing Tetris Game in ASCII Art
This project implements a simple Tetris game rendered in ASCII art that plays itself using a basic AI. The AI uses a heuristic to decide where to place the Tetris pieces on the board.

Code Overview
Board: Initializes the Tetris board.
PrintBoard: Prints the current state of the board to the console.
EmptySpot: Checks if a piece can be placed at a given position.
FitPiece: Places a piece on the board.
WinLine: Removes completed lines from the board.
PickPosition: The AI algorithm that selects the best position for the piece.
RotatePiece: Rotates a Tetris piece.
Score: Evaluates the board state to help the AI make decisions.
GameOn: The main game loop that runs the Tetris game.
