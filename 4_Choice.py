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
    # Calculate available squares
    player_choice = input("Where do you place your mark? ")
    available_square = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    while player_choice not in available_square:
        print("This is not a valid choice. ")
        player_choice = input("Where do you place your mark? ")
    if player_choice in available_square:
        available_square.remove(player_choice)
        return available_square
    return available_square

def transform_choice(player_choice):
    board_squares = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1.0), 5:(1,1), 6:(1,2),\
                          7:(2,0), 8:(2,1), 9:(2,2)}
    board_coordinates = board_squares.get(player_choice)
    return board_coordinates

def update_board(player, board_coordinates, board):
    # adapt board by adding player choice on relevant square
    if board_coordinates == (0,0):
        board[0][0] = player
        print(board)
    elif board_coordinates == (0,1):
        board[0][1] = player
        print(board)
    elif board_coordinates == (0,2):
        board[0][2] = player
        print(board)
    elif board_coordinates == (1,0):
        board[1][0] = player
        print(board)
    elif board_coordinates == (1,1):
        board[1][1] = player
        print(board)
    elif board_coordinates == (1,2):
        board[1][2] = player
        print(board)
    elif board_coordinates == (2,0):
        board[2][0] = player
        print(board)
    elif board_coordinates == (2,1):
        board[2][1] = player
        print(board)
    elif board_coordinates == (2,2):
        board[2][2] = player
        print(board)
    else:
        print("This is not a valid choice.")

    return updated_board

choice()
