# Function for choice of squares
# Function for translating squares into position in board
# Function to activate X or O player
"""
square = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
square_taken = []
choice = input("Where do you place your mark? ")
player = input("Are you player X or player O? ")

def choice():
    if player != 'X' and player != 'O':
        print("This is not a valid choice.")
        break
    if choice in square_taken:
        print("This square is taken.")
        continue
    if player == 'X':
        print('X')
    elif player == 'O':
        print('O')

"""
import pickle
from beautifultable import BeautifulTable   #this creates 3 x 3 table = board

def board_coordinates(square):
    board = BeautifulTable()
    board.append_row(['1', '2', '3'])
    board.append_row(['4', '5', '6'])
    board.append_row(['7', '8', '9'])
    print(board)
    with open('board', mode = 'wb') as my_file:  #this is meant to save the board
        pickle.dump(board, my_file)
    if square == '1':
        return (0,0)
    elif square == '2':
        return (0,1)
    elif square == '3':
        return (0,2)
    elif square == '4':
        return (1,0)
    elif square == '5':
        return (1,1)
    elif square == '6':
        return (1,2)
    elif square == '7':
        return (2,0)
    elif square == '8':
        return (2,1)
    elif square == '9':
        return (2,2)

first_element, second_element = board_coordinates('1')
print(first_element, second_element)
