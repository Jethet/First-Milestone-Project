"""
This function creates the board for tic-tac-toe: nine squares, 3 x 3
A new board must be created each time a player answers 'yes' to the
question if he wants to play.
"""
def create_board():
    print("The board has 3 x 3 = 9 squares."
    " When three squares in a row (horizontal or vertical)"
    " are taken, you win.\n")
    print(' 1 | 2 | 3\n 4 | 5 | 6\n 7 | 8 | 9\n')

create_board()
