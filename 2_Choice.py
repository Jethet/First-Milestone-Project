"""
This is the function that asks the player to choose where to put a mark.
The function first checks if the choice is valid.
"""
import pickle

def choice():
    from beautifultable import BeautifulTable
    board = BeautifulTable()
    board.append_row(['1', '2', '3'])
    board.append_row(['4', '5', '6'])
    board.append_row(['7', '8', '9'])
    print(board, '\n')
    with open('board', mode = 'wb') as my_file:
        pickle.dump(board, my_file)
    player = int(input("Are you player 1 or player 2? "))
    while player == 1 or player == 2:
        square = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        choice = input("Where do you place your mark? ")
        if choice in square and player == 1 or player == 2:
            if choice == '1' and player == 1:
                board[0][0] = 'X'
                square.remove('1')
                print(board)
                with open('board', mode = 'wb') as my_file:
                        pickle.dump(board, my_file)
            elif choice == '1' and player == 2:
                board[0][0] = 'O'
                square.remove('1')
                print(board)
                with open('board', mode = 'wb') as my_file:
                        pickle.dump(board, my_file)
            elif choice == '2' and player == 1:
                board[0][1] = 'O'
                square.remove('2')
                print(board)
                with open('board', mode = 'wb') as my_file:
                        pickle.dump(board, my_file)
            elif choice == '2' and player == 2:
                board[0][1] = 'O'
                square.remove('2')
                print(board)
                with open('board', mode = 'wb') as my_file:
                        pickle.dump(board, my_file)
        print(board)

        return

choice()
