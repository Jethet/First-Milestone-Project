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
    start = input("Would you like to play tic tac toe? Choose 1 for yes and 2 for no. ")
    if start == '2':
        print("Game over.")
    elif start != '1' and start !='2':
        print("This is not a valid entry.")
    else:
        player = int(input("Which player do you want to be: 1 for 'X' and 2 for '0'. "))
        if player == 1:
            print("Player 1 will start: you can choose first.")
        elif player == 2:
            print("You are player 2. Player 1 gets the first turn.")
        else:
            print("This is not a valid entry.")
    try:
        while True:
            square = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] #3 x 3 squares on board
            if ['X', 'X', 'X'] in board:
                print("Player 1 is the winner!")
                break
            elif ['O', 'O', 'O'] in board:
                print("Player 2 is the winner!")
            player = int(input("Are you player 1 or player 2? "))
            if player != 1 and player != 2:
                print("This is not a valid entry")
                break
            choice = input("Where do you place your mark? ")
            if choice == '1' and player == 1:
                board[0][0] = 'X'       #player 1 uses 'X' as mark
                square.remove('1') #the chosen square is no longer an option
                print(board)
            elif choice == '2' and player == 1:
                board[0][1] = 'X'
                square.remove('2')
                print(board)
            elif choice == '3' and player == 1:
                board[0][2] = 'X'
                square.remove('3')
                print(board)
            elif choice == '1' and player == 2:
                board[0][0] = 'O'
                square.remove('1')
                print(board)
            elif choice == '2' and player == 2:
                board[0][1] = 'O'
                square.remove('2')
                print(board)
            elif choice == '3' and player == 2:
                board[0][2] = 'O'
                square.remove('3')
                print(board)
            else:
                print("This is not a valid choice.")
                return
        with open('board', mode = 'wb') as my_file:
            pickle.dump(board, my_file)
    except:
        print("This is not a valid entry.")

choice()
