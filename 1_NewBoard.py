"""
This function creates the board for tic-tac-toe: nine squares, 3 x 3
A new board must be created each time a player answers 'yes' to the
question if he wants to play.Old code:
board = ['1 |', ' 2 |', ' 3\n',  '4 |', ' 5 |', ' 6\n',
        '7 |', ' 8 |', ' 9\n']
print(*board, sep='')
"""

def create_board():
    print("The board has 3 x 3 = 9 squares."
    " Each time you play you can mark one square.\n"
    "The player who gets three marks in a row (diagonal, horizontal or vertical)\n"
    "wins the game.\n")

    from beautifultable import BeautifulTable
    board = BeautifulTable()
    board.append_row(['1', '2', '3'])
    board.append_row(['4', '5', '6'])
    board.append_row(['7', '8', '9'])
    print(board, '\n')

create_board()
