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

def board_coordinates(choice):
    square_taken = []
    if choice == '1':
        square_taken.append('1')
        #print(square_taken)
        return (0,0)
    elif choice == '2':
        square_taken.append('2')
        #print(square_taken)
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

# The function starts here:
def choice():
    square = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    square_taken = []
    while True:
        player = input("Are you player X or player O? ")
        if player != 'X' and player != 'O':
            print("This is not a valid choice.")
            break
            
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
