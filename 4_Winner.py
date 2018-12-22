def winner():
    from beautifultable import BeautifulTable   #this creates 3 x 3 table = board
    board = BeautifulTable()
    board.append_row(['1', '2', '3'])
    board.append_row(['4', '5', '6'])
    board.append_row(['7', '8', '9'])
    print(board)
    board[1][0] = 'X'
    board[1][1] = 'X'
    board[1][2] = 'X'
    if ['X', 'X', 'X'] in board:
        print("Player 1 is the winner!")

winner()
