# This is the function that asks the choice of a player and links to the
# board squares.
# This function is part of main()

import pickle
from beautifultable import BeautifulTable   #this creates 3 x 3 table = board
board = BeautifulTable()
board.append_row(['1', '2', '3'])
board.append_row(['4', '5', '6'])
board.append_row(['7', '8', '9'])
print(board)

# The function starts here:
def choice():

    with open('board', mode = 'wb') as my_file:  #this is meant to save the board
        pickle.dump(board, my_file)
    square = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] #3 x 3 squares on board
    square_taken = []
    while True:
        choice = input("Where do you place your mark? ")
        if choice in square_taken:
            print("This square is taken.")
            continue
        elif choice not in square_taken:
            board_coordinates(choice)
        else:
            print("This is not a valid choice.")
            return
    # Save board changes
    with open('board', mode = 'wb') as my_file:
        pickle.dump(board, my_file)

choice()
