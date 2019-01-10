# This is the function that returns the choice of a square on the board.
# Each time a choice has been made, the board is printed and the player
# is asked if s/he is player X or player O, and what square they choose.
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

    while True:
        player = 'X' or 'O'
        square = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] #3 x 3 squares on board
        if player != 'X' and player != 'O':
            print("This is not a valid choice.")
            break
        player = input("Are you player X or player O? ")
        choice = input("Where do you place your mark? ")
        if choice == '1' and player == 'X':
            board[0][0] = 'X'
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
        elif choice == '8' and player == 'X':
            board[2][1] = 'X'
            square.remove('8')
            print(board)
        elif choice == '9' and player == 'X':
            board[2][2] = 'X'
            square.remove('9')
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
        elif choice == '4' and player == 'O':
            board[1][0] = 'O'
            square.remove('4')
            print(board)
        elif choice == '5' and player == 'O':
            board[1][1] = 'O'
            square.remove('5')
            print(board)
        elif choice == '6' and player == 'O':
            board[1][2] = 'O'
            square.remove('6')
            print(board)
        elif choice == '7' and player == 'O':
            board[2][0] = 'O'
            square.remove('7')
            print(board)
        elif choice == '8' and player == 'O':
            board[2][1] = 'O'
            square.remove('8')
            print(board)
        elif choice == '9' and player == 'O':
            board[2][2] = 'O'
            square.remove('9')
            print(board)
        else:
            print("This is not a valid choice.")
            return
    # Save board changes
    with open('board', mode = 'wb') as my_file:
        pickle.dump(board, my_file)

choice()
