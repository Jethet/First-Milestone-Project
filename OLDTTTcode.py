"""
Missing code: the choice of the square needs to be simplified with function
board_coordinates(). This function generates two values but I do not know how
to get these linked to the board squares ....
"""

import pickle

def choice():
    from beautifultable import BeautifulTable   #this creates 3 x 3 table = board
    board = BeautifulTable()
    board.append_row(['1', '2', '3'])
    board.append_row(['4', '5', '6'])
    board.append_row(['7', '8', '9'])
    print(board)
    with open('board', mode = 'wb') as my_file:  #this is meant to save the board
        pickle.dump(board, my_file)

    start = input("Would you like to play tic tac toe? Choose 1 for yes and 2 for no. ")
    if start == '2':
        print("Game over.")
        return
    elif start != '1' and start !='2':
        print("This is not valid. Please enter 1 or 2.")
        return
    else:
        print("Player X starts the game.")
        with open('board', mode = 'rb') as my_file:
            board = pickle.load(my_file)

    while True:
        square = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        square_taken = []
        player = 'X' or 'O'
        # Two diagonal, three horizontal and three vertical options winner:
        if board[0][0] and board[1][1] == board[2][2] or board[0][2] and \
           board[1][1] == board[2][0] or board[0][0] and board[0][1] == \
           board[0][2] or board[1][0] and board[1][1] == board[1][2] or \
           board[2][0] and board[2][1] == board[2][2] or board[0][0] and \
           board[1][0] == board[2][0] or board[0][1] and board[1][1] \
           == board[2][1] or board[0][2] and board[1][2] == board[2][2]:
            if player == 'X':
                print("Player X is the winner!")
                break
            elif player == 'O':
                print("Player O is the winner!")
                break

        player = input("Are you player X or player O? ")
        if player != 'X' and player != 'O':
            print("This is not a valid choice.")
            break
        choice = input("Where do you place your mark? ")
        if choice in square_taken:
            print("This square is taken.")
            continue
        elif choice not in square_taken:
            if choice == '1' and player == 'X':
                board[0][0] = 'X'
                square_taken.append('1') #the chosen square is no longer an option
                #print(square_taken)
                print(board)
            elif choice == '2' and player == 'X':
                board[0][1] = 'X'
                square_taken.append('2')
                #print(square_taken)
                print(board)
            elif choice == '3' and player == 'X':
                board[0][2] = 'X'
                square_taken.append('3')
                print(board)
            elif choice == '4' and player == 'X':
                board[1][0] = 'X'
                square_taken.append('4')
                print(board)
            elif choice == '5' and player == 'X':
                board[1][1] = 'X'
                square_taken.append('5')
                print(board)
            elif choice == '6' and player == 'X':
                board[1][2] = 'X'
                square_taken.append('6')
                print(board)
            elif choice == '7' and player == 'X':
                board[2][0] = 'X'
                square_taken.append('7')
                print(board)
            elif choice == '8' and player == 'X':
                board[2][1] = 'X'
                square_taken.append('8')
                print(board)
            elif choice == '9' and player == 'X':
                board[2][2] = 'X'
                square_taken.append('9')
                print(board)
            elif choice == '1' and player == 'O':
                board[0][0] = 'O'
                square_taken.append('1')
                print(board)
            elif choice == '2' and player == 'O':
                board[0][1] = 'O'
                square_taken.append('2')
                print(board)
            elif choice == '3' and player == 'O':
                board[0][2] = 'O'
                square_taken.append('3')
                print(board)
            elif choice == '4' and player == 'O':
                board[1][0] = 'O'
                square_taken.append('4')
                print(board)
            elif choice == '5' and player == 'O':
                board[1][1] = 'O'
                square_taken.append('5')
                print(board)
            elif choice == '6' and player == 'O':
                board[1][2] = 'O'
                square_taken.append('6')
                print(board)
            elif choice == '7' and player == 'O':
                board[2][0] = 'O'
                square_taken.append('7')
                print(board)
            elif choice == '8' and player == 'O':
                board[2][1] = 'O'
                square_taken.append('8')
                print(board)
            elif choice == '9' and player == 'O':
                board[2][2] = 'O'
                square_taken.append('9')
                print(board)
            else:
                print("This is not a valid choice.")
                return

choice()
