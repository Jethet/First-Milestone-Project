# This is the function that asks the choice of a player and links to the
# board squares.
# This function is part of main()

import pickle
from beautifultable import BeautifulTable
board = BeautifulTable()
board.append_row(['1', '2', '3'])
board.append_row(['4', '5', '6'])
board.append_row(['7', '8', '9'])
print(board)

# The function starts here:
def choice():
    square = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    square_taken = []
    while True:
        choice = input("Where do you place your mark? ")
        if choice in square_taken:
            print("This square is taken.")
            continue
        if choice not in square_taken:
# HERE the programme should a) determine the coordinates and b) the player
# The board_coordinates can be used for X and for O but how??
# And how to use the function board_coordinates inside choice()??
# This needs to be brought together: get the square and place X or O.

            if player == 'X':
                board_coordinates(choice)
                print('X')
            elif player == 'O':
                board_coordinates(choice)
                print('O')
        else:
            print("This is not a valid choice.")
            return

    # Save board changes
    with open('board', mode = 'wb') as my_file:
        pickle.dump(board, my_file)

choice()
