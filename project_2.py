"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Barbora Mašková
email: baramaskova@seznam.cz
discord: baramaskova
"""

def create_board():
    """
    Creates a 3x3 game board with empty spaces.

    Returns:
        list: A 3x3 matrix with empty strings ' '.
    """
    board = [[' ' for _ in range(3)] for _ in range(3)]
    return board


def display_board(board):
    """
    Draws the game board.

    Args:
        board (list): A 3x3 matrix representing the game board.
    """
    print("+---+---+---+")
    for row in board:
        print("| {} | {} | {} |".format(row[0], row[1], row[2]))
        print("+---+---+---+")


def is_valid_move(board, row, col):
    """
    Checks if a move is valid.

    Args:
        board (list): A 3x3 matrix representing the game board.
        row (int): The row the player is trying to play in.
        col (int): The column the player is trying to play in.

    Returns:
        bool: True if the move is valid, otherwise False.
    """
    if row < 0 or row > 2 or col < 0 or col > 2:
        return False
    if board[row][col] != ' ':
        return False
    return True


def player_move(board, player, move):
    """
    Processes the player's move.

    Args:
        board (list): A 3x3 matrix representing the game board.
        player (str): The current player ('X' or 'O').
        move (int): The move number entered by the player.

    Returns:
        bool: True if the move was successfully made, otherwise False.
    """
    row = (move - 1) // 3
    col = (move - 1) % 3

    if is_valid_move(board, row, col):
        board[row][col] = player
        return True
    else:
        print("Invalid move! Please try again.")
        return False


def get_player_move(player):
    """
    Gets a valid move from the player.

    Args:
        player (str): The current player ('X' or 'O').

    Returns:
        int: A valid move number between 1 and 9.
    """
    while True:
        move = input("Player {} | Please enter your move number: ".format(player)).strip()
        if not move.isdigit():
            print("Invalid input! Please enter a number.")
            continue

        move = int(move)
        if move < 1 or move > 9:
            print("Invalid move! Please enter a number between 1 and 9.")
            continue

        return move


def check_winner(board, player):
    """
    Checks if a player has won.

    Args:
        board (list): A 3x3 matrix representing the game board.
        player (str): The current player ('X' or 'O').

    Returns:
        bool: True if the player has won, otherwise False.
    """
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
                all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
            all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def print_rules():
    """
    Prints the game rules.
    """
    print("Welcome to Tic Tac Toe")
    print(44 * "=")
    print("GAME RULES:")
    print(
        "Each player can place one mark (or stone)\nper turn on the 3x3 grid. The WINNER is\nwho succeeds in placing three of their\nmarks in a:")
    print("* horizontal,")
    print("* vertical or")
    print("* diagonal row")
    print(44 * "=")
    print("Let's start the game")
    print(44 * "_")


def initialize_game():
    """
    Initializes the game board and returns it.

    Returns:
        list: A 3x3 matrix representing the initialized game board.
    """
    board = create_board()
    display_board(board)
    return board


def game_loop(board, players):
    """
    The main game loop. Processes player moves and checks for a winner or a draw.

    Args:
        board (list): A 3x3 matrix representing the game board.
        players (list): A list of players ['X', 'O'].
    """
    turn = 0
    while True:
        player = players[turn % 2]
        move = get_player_move(player)
        if player_move(board, player, move):
            display_board(board)
            if check_winner(board, player):
                print("Congratulations, the player {} WON!".format(player))
                break
            if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
                print("It's a draw!")
                break
            turn += 1


def main():
    """
    The main function of the game. Prints the rules, initializes the game, and starts the game loop.
    """
    print_rules()
    board = initialize_game()
    players = ['O', 'X']
    game_loop(board, players)


if __name__ == "__main__":
    main()
