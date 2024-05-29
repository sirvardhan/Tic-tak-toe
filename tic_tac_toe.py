import random

def print_board(board):
    print("Current board:")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def check_draw(board):
    return all(cell != " " for row in board for cell in row)

def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move // 3][move % 3] == " ":
                board[move // 3][move % 3] = "X"
                break
            else:
                print("Cell already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Enter a number between 1 and 9.")

def computer_move(board):
    while True:
        move = random.randint(0, 8)
        if board[move // 3][move % 3] == " ":
            board[move // 3][move % 3] = "O"
            break

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        player_move(board)
        print_board(board)
        if check_winner(board, "X"):
            print("Congratulations! You win!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

        computer_move(board)
        print_board(board)
        if check_winner(board, "O"):
            print("Computer wins! Better luck next time.")
            break
        if check_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    tic_tac_toe()
