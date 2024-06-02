"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Barbora Mašková
email: baramaskova@seznam.cz
discord: baramaskova
"""

# funkce pro hrací pole
def create_board():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    return board

# fce pro vykresleni hraciho pole
def display_board(board):
    print("+---+---+---+")
    for row in board:
        print("| {} | {} | {} |".format(row[0], row[1], row[2]))
        print("+---+---+---+")

#fce pro overeni tahu
def is_valid_move(board, row, col):
    if row < 0 or row > 2 or col < 0 or col > 2:
        return False
    if board[row][col] != ' ':
        return False
    return True

# fce pro tah hrace
def player_move(board, player):
    while True:
        move = input("Player {} | Please enter your move number: ".format(player))
        if not move.isdigit():
            print("Invalid input! Please enter a number.")
            continue

        move = int(move)
        if move < 1 or move > 9:
            print("Invalid move! Please enter a number between 1 and 9.")
            continue

        row = (move - 1) // 3
        col = (move - 1) % 3

        if is_valid_move(board, row, col):
            board[row][col] = player
            break
        else:
            print("Invalid move! Please try again.")


# fce na overeni viteze (horizontal, vertical or diagonal row)
def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def main():
    print("Welcome to Tic Tac Toe")
    print(44 * "=")
    print("GAME RULES:")
    print("Each player can place one mark (or stone)\nper turn on the 3x3 grid. The WINNER is\nwho succeeds in placing three of their\nmarks in a:")
    print("* horizontal,")
    print("* vertical or")
    print("* diagonal row")
    print(44 * "=")
    print("Let's start the game")
    print(44 * "_")
    board = create_board()
    display_board(board)

    players = ['X', 'O']
    turn = 0

    while True:
        player = players[turn % 2]
        player_move(board, player)
        display_board(board)
        if check_winner(board, player):
            print("Congratulations, the player {} WON!".format(player))
            break
        if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
            print("It's a draw!")
            break
        turn += 1

if __name__ == "__main__":
    main()