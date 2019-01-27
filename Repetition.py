# Function for translating squares into position in board
# Function to activate X or O player

board_squares = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2),\
                      7:(2,0), 8:(2,1), 9:(2,2)}
player_choice = int(input("Where do you place your mark? "))
##print(player_choice)
board_coordinates = board_squares.get(player_choice)
print(board_coordinates)



"""
import pickle
from beautifultable import BeautifulTable   #this creates 3 x 3 table = board
square = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
square_taken = []


def board_coordinates(choice):
    board = BeautifulTable()
    board.append_row(['1', '2', '3'])
    board.append_row(['4', '5', '6'])
    board.append_row(['7', '8', '9'])
    print(board)
    with open('board', mode = 'wb') as my_file:  #this is meant to save the board
        pickle.dump(board, my_file)
        while True:
            player = input("Are you player X or player O? ")
            if player != 'X' and player != 'O':
                print("This is not a valid choice.")
                break
            choice = input("Where do you place your mark? ")
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

first_element, second_element = board_coordinates('1')
print(first_element, second_element)

board_coordinates(square)
"""
