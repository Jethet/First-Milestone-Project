"""
This is the main() function of the code for the game TicTacToe.
Two players can play the game, sitting at the same computer.
The board should be printed out every time a player has made a move.
The programme should accept input from the player, determine the
position and then place a symbol on the board. Subsequently, that
position should not be available anymore.
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
    if player != 'X' and player != 'O':
        print("This is not a valid choice.")
        break
    else:
        player == 'X' or player == 'O'

# If the player wants to play, a new board is created.
def new_board():
    from beautifultable import BeautifulTable
    board = BeautifulTable()
    board.append_row(['1', '2', '3'])
    board.append_row(['4', '5', '6'])
    board.append_row(['7', '8', '9'])
    print(board, '\n')

# Player can choose a square.
# If player chooses a square, the choice is shown on the board.
# The chosen square should be blocked.
choice()

# The player who gets three marks in a row is declared the winner.
winner()
