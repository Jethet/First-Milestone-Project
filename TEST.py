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
    with open('board', mode = 'wb') as my_file:  #this is meant to save the board
        pickle.dump(board, my_file)
        player = int(input("Are you player 1 or player 2? "))
        while player == 1 or player == 2:
            print(board)
            square = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] #3 x 3 squares on board
            choice = input("Where do you place your mark? ")
            if choice in square:
                with open('board', mode = 'rb') as my_file:
                    board = pickle.load(my_file)    #this is meant to open the board
                    if choice == 1 and player == 1:
                        board[0][0] = 'X'       #player 1 uses 'X' as mark
                        square.remove('1')      #the chosen square is no longer an option
                        print(board)            #the new board with 'X' is printed
                        with open('board', mode = 'wb') as my_file:
                            pickle.dump(board, my_file)   #the new board is saved
                    elif choice == 1 and player == 2:
                        board[0][0] = 'O'
                        square.remove('1')
                        print(board)
                        with open('board', mode = 'wb') as my_file:
                            pickle.dump(board, my_file)
            else:
                print("Choose between 1 and 2. ")
        else:
            print("This is not a valid choice.")

choice()
