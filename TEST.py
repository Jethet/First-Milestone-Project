import pickle

def choice():
    try:
        from beautifultable import BeautifulTable
        board = BeautifulTable()
        board.append_row(['1', '2', '3'])
        board.append_row(['4', '5', '6'])
        board.append_row(['7', '8', '9'])
        print(board, '\n')
        with open('board', mode = 'wb') as my_file:
            pickle.dump(board, my_file)
            game = False
            while game == False:
                square = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                player = int(input("Are you player 1 or player 2? "))
                choice = int(input("Where do you place your mark? "))
                if choice in square and player == 1 or player == 2:
                    with open('board', mode = 'rb') as my_file:
                        board = pickle.load(my_file)
                        if choice == 1 and player == 1:
                            board[0][0] = 'X'
                            square.remove(1)
                            print(board)
                            with open('board', mode = 'wb') as my_file:
                                pickle.dump(board, my_file)

                        elif choice == 1 and player == 2:
                            with open('board', mode = 'rb') as my_file:
                                board = pickle.load(my_file)
                                board[0][0] = 'O'
                                square.remove(1)
                                print(board)
                                with open('board', mode = 'wb') as my_file:
                                        pickle.dump(board, my_file)

                else:
                    print("Choose between 1 and 2. ")
            game = False
    except:
        print("Please enter a number. ")
"""
            elif choice == 2:
            board[0][1] = 'X'
            print(board)
        elif choice == 3:
            board[0][2] = 'X'
            print(board)
        elif choice == 4:
            board[1][0] = 'X'
            print(board)
"""


choice()
