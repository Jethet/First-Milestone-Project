def choice():
    from beautifultable import BeautifulTable
    board = BeautifulTable()
    board.append_row(['1', '2', '3'])
    board.append_row(['4', '5', '6'])
    board.append_row(['7', '8', '9'])
    print(board, '\n')
    square = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    choice = int(input("Where do you place your mark? "))
    while choice in square:
        if choice == 1:
            board[0][0] = 'X'
            print(board)
        elif choice == 2:
            board[0][1] = 'X'
            print(board)
        break
    return board


choice()
