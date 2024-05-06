#!/usr/bin/python3
def print_board(board):
    """
    Function to print the Tic Tac Toe board.

    Parameters:
        board (list of lists): The Tic Tac Toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Function to check if there is a winner in the Tic Tac Toe game.

    Parameters:
        board (list of lists): The Tic Tac Toe board.

    Returns:
        bool: True if there is a winner, False otherwise.
    """
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    """
    Function to play the Tic Tac Toe game.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            if row < 0 or row > 2 or col < 0 or col > 2:  # Check if row and column are within the range
                print("Invalid input. Row and column values must be between 0 and 2.")
                continue
            if board[row][col] == " ":
                board[row][col] = player
                if check_winner(board):
                    break  # Exit loop if there's a winner
                if player == "X":
                    player = "O"
                else:
                    player = "X"
            else:
                print("That spot is already taken! Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print_board(board)
    if player == "X":
        winner = "O"
    else:
        winner = "X"
    print("Player " + winner + " wins!")

tic_tac_toe()
