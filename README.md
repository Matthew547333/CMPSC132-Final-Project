# CMPSC132-Final-Project
# Tic-Tac-Toe Game

A two-player, terminal-based Tic-Tac-Toe game built in Python for CMPSC 132.

## Project Description

This program implements a classic 3x3 Tic-Tac-Toe game that runs entirely in the terminal. Two players take turns entering moves as Player X and Player O. The game validates every move, prevents illegal plays, and automatically detects wins across all rows, columns, and diagonals, as well as draw conditions when the board is full.

The project applies core Python concepts covered in CMPSC 132, including functions, lists of lists as a 2D data structure, input validation, and control flow logic.

## Features

- 3x3 game board displayed in the terminal after every move
- Two-player turn alternation (X goes first)
- Input validation — rejects out-of-range coordinates and already-occupied cells
- Win detection across all rows, columns, and both diagonals
- Draw detection when the board is full with no winner
- Clean, readable output throughout the game

## Requirements

- Python 3.x
- No external libraries required

## How to Run

1. Clone or download this repository:

```
git clone <your-repo-url>
cd <repo-folder>
```

2. Run the game from your terminal:

```
python tictactoe.py
```

3. Follow the on-screen prompts. When it is your turn, enter your desired **row** and **column** as integers between `0` and `2`:

```
Player X, enter row (0-2): 1
Player X, enter column (0-2): 1
```

4. The game ends when a player wins or the board is full (draw).

## Board Layout

Positions are referenced by row and column, both numbered 0 through 2:

```
     Col 0  Col 1  Col 2
Row 0  [0,0] [0,1] [0,2]
Row 1  [1,0] [1,1] [1,2]
Row 2  [2,0] [2,1] [2,2]
```

Example mid-game board display:

```
 X | O | X
-----------
   | X |  
-----------
 O |   | O
```

## Project Structure

```
tictactoe.py   - Main source file containing all game logic
README.md      - Project description and instructions
```

## Key Functions

| Function | Description |
|---|---|
| `print_board(board)` | Displays the current 3x3 board in the terminal |
| `check_winner(board, player)` | Returns `True` if the given player has won |
| `is_draw(board)` | Returns `True` if the board is full with no winner |
| `get_move(player)` | Prompts the current player for a valid row and column |
| `play_game()` | Main game loop — alternates turns until the game ends |

## Data Structures Used

- **List of lists** — the board is represented as a 3x3 nested list, e.g. `board = [[' ', ' ', ' '] for _ in range(3)]`, allowing easy row, column, and diagonal traversal.
- **Strings** — each cell holds `'X'`, `'O'`, or `' '` (empty).

## Author

Matthew — CMPSC 132, Penn State
