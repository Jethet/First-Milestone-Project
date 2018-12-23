# This function creates the board for TicTacToe: nine squares, 3 x 3
# A new board must be created each time a player answers 'yes' to the
# question if he wants to play.

def new_board():
    from beautifultable import BeautifulTable
    board = BeautifulTable()
    board.append_row(['1', '2', '3'])
    board.append_row(['4', '5', '6'])
    board.append_row(['7', '8', '9'])
    print(board, '\n')

new_board()
