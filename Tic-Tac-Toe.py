# Tic-Tac-Toe Game
"""
TODO: Input the team number and names of the team members here.
Team Number:
Team Member 1:
Team Member 2:
"""


# Initialize the board
def initialize_board():
    """
    Initialize the board with empty spaces
    Parameters:
            None
    Returns:
            list: The board with empty spaces
    """
    return [' '] * 9


# Display the board
def display_board(board):
    """
    Display the board on the screen
    Parameters:
            board (list): The current board
    Returns:
            None
    """
    print("\n " + board[0] + " | " + board[1] + " | " + board[2] + " ")
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")


# Check if the board is full
def is_board_full(board):
    """
    Check if the board is full (no empty spaces)
    Parameters:
            board (list): The current board
    Returns:
            bool: True if the board is full, False otherwise
    """
    # TODO: Implement this function
    pass


# Check for a win
def check_win(board, player):
    """
    Check if the player has won in any of the possible ways/conditions
    Parameters:
            board (list): The current board
            player (str): The player ("X" or "O")
    Returns:
            bool: True if the player has won, False otherwise
    """

    # TODO: Implement this function
    # TODO 1: check rows

    # TODO 2: check columns

    # TODO 3: check diagonals

    # the function will return False if any the previous checks are not returning True
    return False



# Get player input
def get_player_input(board, player):
    """
    Get the player's move and check if it is valid
    Parameters:
        board (list): The current board
        player (str): The player ("X" or "O")
    Returns:
        int: The position of the player's move
    """

    while True:
        print("\nThe current player is: " + player)
        move = input("Enter your move (1-9): ")
        # TODO 1: Check if the input is valid (1-9 and not already taken)

        # TODO 2: Return the position for the move, which should be within range 0 - 8
        return int(move) - 1



    # Main game loop
def play_game():
    """
    The main game loop where the game is played until completion
    """
    while True:
        board = initialize_board()
        player = "X"

        while True:
            display_board(board)
            move = get_player_input(board, player=player)
            board[move] = player

            # TODO 1: Check if any player has won
            pass

            # TODO: Check if the board is full and it is a draw
            # Note: this portion has been comppleted for you
            if is_board_full(board):
                display_board(board)
                print("It's a draw!")
                break

            # TODO 2: Switch players if game is not over
            pass

        # prompting user if they want to start a new game, otherwise do not start a new game
        play_again = input("Do you want to play again? (Y/N): ").upper()
        if play_again != 'Y':
            break


# This is the main function. You do not need to make any changes here
def main():
    """
    Main function to run the game.
    """
    print("Welcome to Tic-Tac-Toe!")
    play_game()
    print("Thanks for playing!")

if __name__ == "__main__":
    main()