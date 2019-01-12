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

# Number that player chooses needs to be translated into position on 3 x 3 board
def board_coordinates(choice):
    while True:
        choice = input("Where do you place your mark? ")
        if choice == '1':
            square_taken.append('1')
            return (0,0)
        elif choice == '2':
            square_taken.append('2')
            return (0,1)
        elif choice == '3':
            square_taken.append('3')
            return (0,2)
        elif choice == '4':
            square_taken.append('4')
            return (1,0)
        elif choice == '5':
            square_taken.append('5')
            return (1,1)
        elif choice == '6':
            square_taken.append('6')
            return (1,2)
        elif choice == '7':
            square_taken.append('7')
            return (2,0)
        elif choice == '8':
            square_taken.append('8')
            return (2,1)
        elif choice == '9':
            square_taken.append('9')
            return (2,2)
        # Save board changes
        with open('board', mode = 'wb') as my_file:
            pickle.dump(board, my_file)

# The player who gets three marks in a row is declared the winner.
winner()
