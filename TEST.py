#This function creates the board for tic-tac-toe: nine squares, 3 x 3
#A new board must be created each time a player answers the question
#which player he chooses.

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
        player = int(input("Are you player 1 or player 2? "))
        if player != 1 and player != 2:
                print("Choose between 1 and 2. ")
        while player == 1 or player == 2:
            square = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] #3 x 3 squares on board
            choice = input("Where do you place your mark? ")
            while choice in square and player == 1:
                if choice == '1':
                    board[0][0] = 'X'       #player 1 uses 'X' as mark
                    square.remove('1')      #the chosen square is no longer an option
                    print(board)
                    with open('board', mode = 'wb') as my_file:
                            pickle.dump(board, my_file)           #the new board with 'X' is printed
                elif choice == '2':
                    board[0][1] = 'X'
                    square.remove('2')
                    print(board)
                    with open('board', mode = 'wb') as my_file:
                            pickle.dump(board, my_file)
            while choice in square and player == 2:
                if choice == '1':
                    board[0][0] = 'O'
                    square.remove('1')
                    print(board)
                    with open('board', mode = 'wb') as my_file:
                            pickle.dump(board, my_file)
                elif choice == '2':
                    board[0][1] = 'O'
                    square.remove('2')
                    print(board)
                    with open('board', mode = 'wb') as my_file:
                            pickle.dump(board, my_file)

        else:
            print("This is not a valid choice.")
            return

choice()
