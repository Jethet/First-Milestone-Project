# Player can choose a square.
# If player chooses a square, the choice is shown on the board.
# The chosen square should be blocked.
# If the choice is not valid, player chooses again.

def choice(player, board):
    # make a list of squares that can be chosen
    list_available_squares = open_square(board)
    # ask the player for her/his choice
    player_choice = input("Where do you place your mark? ")
    # check if choice is in the list of squares
    # if choice not in list of squares, player must choose again
    while player_choice not in list_available_squares:
        print("This square is taken. ")
        player_choice = input("Where do you place your mark? ")
    # choice is translated into board_coordinates
    board_coordinates = transform_choice(choice)
    # show choice on the board
    updated_board = update_board(player, board_coordinates, board)
    print(updated_board)
    return updated_board


def open_square(board):
    available_square = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    # TO DO: calculate available squares
    return available_square

def transform_choice(choice):
    # TO DO: write board_coordinates
    return (0,0)

def update_board(player, board_coordinates, board):
    # adapt board by adding player choice on relevant square
    # TO DO: code for updating board
    return updated_board
