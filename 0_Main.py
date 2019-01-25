"""
This is the main() function of the code for the game TicTacToe.
Two players can play the game, sitting at the same computer.
The board should be printed every time a player has made a move.
The programme should accept input from the player, determine the
position and then place a symbol on that board position. Subsequently,
that position should not be available anymore.
The player who is the first to have three (X or O) in a row, is the winner.
"""

# This is an explanation of the game.
print("The board has 3 x 3 = 9 squares. You can play with X or with O."
" Each time you play you can mark one square.\n"
"The player who gets three marks in a row (diagonal, horizontal or vertical)\n"
"wins the game.\n")

import pickle
# Pickle is used to save all the  changes to the board during the game.
with open('board', mode = 'wb') as my_file:  #this saves the board
    pickle.dump(board, my_file)

# First step is ask players if they want to play.
# Player is asked to choose X or O; player X starts.
def player():
    player = input("Are you player X or player O? ")
    while player != 'X' and player != 'O':
        print("This is not a valid choice. ")
        player = input("Are you player X or player O? ")
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

# Player can choose a square.
# If player chooses a square, the choice is shown on the board.
# The chosen square should be blocked.
def choice(player, board):
    # ask the player for her/his choice
    player_choice = input("Where do you place your mark? ")

    # make a list of squares that can be chosen
    # check if choice is in the list of squares
    # if choice not in list of squares, player must choose again
    list_available_squares = open_square()

    # choice is translated into board_coordinates
    board_coordinates = transform_choice(choice)
    # show choice on the board
    updated_board = update_board(player, board_coordinates, board)
    print(updated_board)
    return updated_board
"""
The following functions have been created new: open_square(), transform_choice()
and update_board()
Originally, 'board' was added as parameter in open_square() but I have taken
this out because I do not think it is necessary.
"""
def open_square():
    player_choice = input("Where do you place your mark? ")
    available_square = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    while player_choice not in available_square:
        print("This is not a valid choice. ")
        player_choice = input("Where do you place your mark? ")

    if player_choice in available_square:
        available_square.remove(player_choice)
        return available_square

def transform_choice(choice):
    # TO DO: write board_coordinates
    return (0,0)

def update_board(player, board_coordinates, board):
    # adapt board by adding player choice on relevant square
    # TO DO: code for updating board
    return updated_board

# The player who gets three marks in a row is declared the winner.
def winner(board):
    if board[0][0] and board[1][1] == board[2][2] or board[0][2] and \
       board[1][1] == board[2][0] or board[0][0] and board[0][1] == \
       board[0][2] or board[1][0] and board[1][1] == board[1][2] or \
       board[2][0] and board[2][1] == board[2][2] or board[0][0] and \
       board[1][0] == board[2][0] or board[0][1] and board[1][1] \
       == board[2][1] or board[0][2] and board[1][2] == board[2][2]:
        if player == 'X':
            print("Player X is the winner!")
            return 'X'
        elif player == 'O':
            print("Player O is the winner!")
            return 'O'
