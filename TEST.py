def choice():
    from beautifultable import BeautifulTable
    board = BeautifulTable()
    board.append_row(['1', '2', '3'])
    board.append_row(['4', '5', '6'])
    board.append_row(['7', '8', '9'])
    print(board, '\n')

    try:
        game = False
        while game == False:
            square = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            player = int(input("Are you player 1 or player 2? "))
            choice = int(input("Where do you place your mark? "))
            if choice in square:
                if choice == 1 and player == 1:
                    board[0][0] = 'X'
                    square.remove(1)
                    print(board)
                elif choice == 1 and player == 2:
                    board[0][0] = 'O'
                    square.remove(1)
                    print(board)                    
        game = False
    except:
        print("Please choose a number between 1 and 9. ")
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
