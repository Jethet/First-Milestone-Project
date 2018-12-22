
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
        print("This is not valid. Please enter 1 or 2.")
    else:
        print("Player 1 starts the game.")
    try:
        while True:
            square = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] #3 x 3 squares on board
            player = input("Are you player X or player O? ")
            if player != 'X' and player != 'O':
                print("This is not a valid choice.")
                break
            if ['X', 'X', 'X'] in board:
                print("Player 1 is the winner!")
                break
            elif ['O', 'O', 'O'] in board:
                print("Player 2 is the winner!")
                break
            elif board.columns(0) == ['X', 'X', 'X']:
                print("Player 1 is the winner!")
                break
            choice = input("Where do you place your mark? ")
            if choice == '1' and player == 'X':
                board[0][0] = 'X'       #player 1 uses 'X' as mark
                square.remove('1') #the chosen square is no longer an option
                print(board)
            elif choice == '2' and player == 'X':
                board[0][1] = 'X'
                square.remove('2')
                print(board)
            elif choice == '3' and player == 'X':
                board[0][2] = 'X'
                square.remove('3')
                print(board)
            elif choice == '4' and player == 'X':
                board[1][0] = 'X'
                square.remove('4')
                print(board)
            elif choice == '5' and player == 'X':
                board[1][1] = 'X'
                square.remove('5')
                print(board)
            elif choice == '6' and player == 'X':
                board[1][2] = 'X'
                square.remove('6')
                print(board)
            elif choice == '7' and player == 'X':
                board[2][0] = 'X'
                square.remove('7')
                print(board)
            elif choice == '1' and player == 'O':
                board[0][0] = 'O'
                square.remove('1')
                print(board)
            elif choice == '2' and player == 'O':
                board[0][1] = 'O'
                square.remove('2')
                print(board)
            elif choice == '3' and player == 'O':
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
