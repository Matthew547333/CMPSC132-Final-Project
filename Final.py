def make_board():
    """
    Creates and returns a fresh 3x3 board as a list of lists.
    Each cell is initialized to a single space ' '.
 
        >>> b = make_board()
        >>> len(b)
        3
        >>> len(b[0])
        3
        >>> b[0][0]
        ' '
    """
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    return board
 
 
def print_board(board):
    """
    Prints the current state of the board to the terminal.
    Rows are separated by dividers and columns by '|'.
 
        >>> b = make_board()
        >>> b[0][0] = 'X'
        >>> b[1][1] = 'O'
        >>> print_board(b)
        <BLANKLINE>
          0   1   2
        0 X | _ | _
          ---------
        1 _ | O | _
          ---------
        2 _ | _ | _
        <BLANKLINE>
    """
    print()
    print('  0   1   2')
    for row_index in range(3):
        row = board[row_index]
        display = []
        for cell in row:
            if cell == ' ':
                display.append('_')
            else:
                display.append(cell)
        print(f'{row_index} {display[0]} | {display[1]} | {display[2]}')
        if row_index < 2:
            print('  ---------')
    print()
 
 
def check_winner(board, player):
    """
    Returns True if the given player ('X' or 'O') has won the game.
    Checks all rows, columns, and both diagonals.
 
        >>> b = make_board()
        >>> b[0] = ['X', 'X', 'X']
        >>> check_winner(b, 'X')
        True
        >>> check_winner(b, 'O')
        False
        >>> b2 = make_board()
        >>> b2[0][0] = 'O'
        >>> b2[1][1] = 'O'
        >>> b2[2][2] = 'O'
        >>> check_winner(b2, 'O')
        True
        >>> b3 = make_board()
        >>> b3[0][1] = 'X'
        >>> b3[1][1] = 'X'
        >>> b3[2][1] = 'X'
        >>> check_winner(b3, 'X')
        True
    """
    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            return True
 
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
 
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
 
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
 
    return False
 
 
def is_draw(board):
    """
    Returns True if the board is completely full and there is no winner.
    Does NOT check for a winner — assumes check_winner was already called.
 
        >>> b = make_board()
        >>> is_draw(b)
        False
        >>> b2 = [['X','O','X'],['O','X','O'],['O','X','O']]
        >>> is_draw(b2)
        True
    """
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True
 
 
def is_valid_move(board, row, col):
    """
    Returns True if placing a piece at (row, col) is a legal move.
    A move is valid if:
      - row and col are integers in range 0-2
      - the chosen cell is currently empty
 
        >>> b = make_board()
        >>> is_valid_move(b, 0, 0)
        True
        >>> b[0][0] = 'X'
        >>> is_valid_move(b, 0, 0)
        False
        >>> is_valid_move(b, 3, 0)
        False
        >>> is_valid_move(b, 0, -1)
        False
    """
    if row < 0 or row > 2 or col < 0 or col > 2:
        return False
    if board[row][col] != ' ':
        return False
    return True
 
 
def get_player_move(board, player):
    """
    Prompts the current player to enter a row and column.
    Keeps asking until a valid move is entered.
    Returns (row, col) as a tuple of integers.
    """
    print(f"Player {player}'s turn.")
    row_input = input("  Enter row (0-2): ")
    col_input = input("  Enter column (0-2): ")
 
    if not row_input.isdigit() or not col_input.isdigit():
        print("  Invalid input. Please enter whole numbers between 0 and 2.\n")
        return get_player_move(board, player)
 
    row = int(row_input)
    col = int(col_input)
 
    if not is_valid_move(board, row, col):
        print("  That move is not allowed. The cell may be occupied or out of range.\n")
        return get_player_move(board, player)
 
    return row, col
 
 
def switch_player(current_player):
    """
    Returns the other player's symbol.
 
        >>> switch_player('X')
        'O'
        >>> switch_player('O')
        'X'
    """
    if current_player == 'X':
        return 'O'
    return 'X'
 
 
def play_round(board, current_player):
    """
    Plays a single round of the game (one full game from start to finish).
    Returns nothing. Called recursively to ask play again.
    """
    print_board(board)
    row, col = get_player_move(board, current_player)
    board[row][col] = current_player
 
    if check_winner(board, current_player):
        print_board(board)
        print(f"*** Player {current_player} wins! Congratulations! ***\n")
 
    elif is_draw(board):
        print_board(board)
        print("*** It's a draw! Well played by both! ***\n")
 
    else:
        play_round(board, switch_player(current_player))
 
 
def play_game():
    """
    Main game loop. Runs a complete two-player Tic-Tac-Toe game.
    Alternates turns between Player X and Player O.
    Ends when a player wins or the game is a draw.
    Asks if players want to play again after each game.
    """
    print("=" * 35)
    print("   Welcome to Tic-Tac-Toe!")
    print("   Player 1 = X    Player 2 = O")
    print("=" * 35)
 
    play_round(make_board(), 'X')
 
    again = input("Play again? (yes/no): ").strip().lower()
    if again == 'yes' or again == 'y':
        play_game()
    else:
        print("\nThanks for playing! Goodbye!")
 
 
def run_tests():
    import doctest
    doctest.testmod(verbose=True)
 
 
if __name__ == "__main__":
    play_game()