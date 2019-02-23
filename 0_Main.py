"""
DESCRIPTION
This is the main() function of the code for the game Tic Tac Toe.
Two players can play the game, sitting at the same computer.
The board should be printed every time a player has made a move.
The programme should accept input from the player, determine the
position and then place a symbol for the player (eigher X or O)
on that board position. Subsequently, that position should not be
available anymore. The player who is the first to have three (X or O)
in a row is the winner.
"""

# Pickle is used to save all the  changes to the board during the game.
# Player is asked to choose X or O; player X starts.
#import pickle

playing = True

# The player is asked if s/he wants to play:
def start_game():
    start = input("Would you like to play Tic Tac Toe? Choose 1 for yes\
 and 2 for no. ")
    while start != '1' and start != '2':
        print("This is not valid. Please enter 1 or 2.")
        start = input("Choose 1 for yes and 2 for no. ")
    else:
        if start == '1':
            print("Let's play!")
        elif start == '2':
            print("Game over!")
            playing = False
            exit()

# The player is asked what mark (X or O) s/he wants to use:
def get_player():
    print("In Tic Tac Toe, player X starts the game.")
    player = input("Are you player X or player O? ")
    while player != 'X' and player != 'O':
        print("This is not a valid choice. ")
        player = input("Are you player X or player O? ")
    else:
        return player

# If the player wants to play, a new board is created.
def new_board():
    from beautifultable import BeautifulTable
    board = BeautifulTable()
    board.append_row(['1', '2', '3'])
    board.append_row(['4', '5', '6'])
    board.append_row(['7', '8', '9'])
    print(board, '\n')
    return board

# The player is asked to choose a square to put her/his mark:
def open_square():
    available_square = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    player_choice = input("Where do you place your mark? ")
    try:
        if not player_choice in available_square:
            print("This is not a valid choice. ")
        #player_choice = input("Where do you place your mark? ")
    except:
        print("This is not a valid choice. ")
    available_square.remove(player_choice)
    return available_square

# The choice is transformed into board board_coordinates:
def transform_choice(player_choice):
    board_squares = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1.0), 5:(1,1), 6:(1,2),\
                          7:(2,0), 8:(2,1), 9:(2,2)}
    board_coordinates = board_squares.get(player_choice)
    return board_coordinates

# The board is updated by adding player choice on relevant square
def update_board(player, board_coordinates, board):
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
    return board

# Player can choose a square.
# If player chooses a square, the choice is shown on the board.
# The chosen square should be blocked.
def get_choice(player, board):
    # ask the player for her/his choice
    player_choice = input("Where do you place your mark? ")

    # make a list of squares that can be chosen
    # check if choice is in the list of squares
    # if choice not in list of squares, player must choose again
    available_squares = open_square()

    # choice is translated into board_coordinates
    board_coordinates = transform_choice(player_choice)
    # show choice on the board
    board = update_board(player, board_coordinates, board)
    print(board)
    return board

# The player who gets three marks in a row is declared the winner.
def check_winner(board):
    if board[0][0] and board[1][1] == board[2][2] or board[0][2] and \
       board[1][1] == board[2][0] or board[0][0] and board[0][1] == \
       board[0][2] or board[1][0] and board[1][1] == board[1][2] or \
       board[2][0] and board[2][1] == board[2][2] or board[0][0] and \
       board[1][0] == board[2][0] or board[0][1] and board[1][1] \
       == board[2][1] or board[0][2] and board[1][2] == board[2][2]:
       return True
    else:
        print("It is a tie!")  # IF THE CHECK FOR A WINNER IS DONE EACH TIME
        return False            # THE PLAYER CHOOSES A SQUARE, THERE WILL BE
                                # MANY TIMES THAT 3-IN-A-ROW IS NOT True
                                # The message 'It is a tie!' should not be
                                # printed EVERY time
# When the game ends, the player is asked if s/he wants to play again:
def repeat_game():
    answer = input("Would you like to play again? Choose 1 for yes and 2 for no. ")
    while answer != '1' and answer != '2':
        print("This is not valid. Please enter 1 or 2.")
        answer = input("Choose 1 for yes and 2 for no. ")
    else:
        if answer == '1':
            print("Let's play!")
        elif answer == '2':
            print("Thanks for player, until next time!")
            playing = False
            exit()

def main():
    while playing == True:
    # This is an explanation of the game.
        print("In Tic Tac Toe, the board has 3 x 3 = 9 squares. You can be player X or O.\n"
        "Player X starts the game. Each time you play you can mark one square.\n"
        "The player who gets three marks in a row (diagonal, horizontal or vertical)\n"
        "wins the game.\n")
        # First step is ask players if they want to play:
        start = start_game()
        # Second step: player chooses X or O:
        player = get_player()
        # Third step: board is printed:
        board = new_board()
        #with open('board', mode = 'wb') as handle:  #this saves the board
        #    pickle.dump(board, handle)
        # Fourth step: player chooses square, square is checked and if available
        # square is marked with X or O and updated board is printed:
        choice = get_choice(player,board)
        #with open('board', mode = 'rb') as handle:
        #    board = pickle.load(handle)
        # Fifth step is check if there is a winner. For this there must be three
        # squares with the same mark in one row (horizontal, vertical or diagonal)
        winner = check_winner(board)
        repeat = repeat_game()

#with open('board', mode = 'wb') as my_file:  #this saves the board
#    pickle.dump(board, my_file)

main()
