# This function returns a 'winner!' message if a player has won the game.
# There are many options for getting three X or three O in a row: horizontal,
# vertical or diagonal.
# This function is part of main()

def winner():
    # Two options diagonal across with XXX:
    if board[0][0] and board [1][1] and board[2][2] == 'X':
        print("Player X is the winner!")
        break
    elif board[0][2] and board[1][1] and board[2][0] == 'X':
        print("Player X is the winner!")
        break
    # Two options diagonal across with OOO:
    if board[0][0] and board [1][1] and board[2][2] == 'O':
        print("Player O is the winner!")
        break
    elif board[0][2] and board[1][1] and board[2][0] == 'O':
        print("Player O is the winner!")
        break
    # Three options for vertical columns with XXX:
    if board[0][0] and board[1][0] and board[2][0] == 'X':
        print("Player X is the winner!")
        break
    elif board[0][1] and board[1][1] and board[2][1] == 'X':
        print("Player X is the winner!")
        break
    elif board[0][2] and board[1][2] and board[2][2] == 'X':
        print("Player X is the winner!")
        break
    # Three options for vertical columns with OOO:
    elif board[0][0] and board[1][0] and board[2][0] == 'O':
        print("Player O is the winner!")
        break
    elif board[0][1] and board[1][1] and board[2][1] == 'O':
        print("Player X is the winner!")
        break
    elif board[0][2] and board[1][2] and board[2][2] == 'O':
        print("Player X is the winner!")
        break
    # Horizontal XXX and OOO options:
    elif ['X', 'X', 'X'] in board:
        print("Player X is the winner!")
        break
    elif ['O', 'O', 'O'] in board:
        print("Player X is the winner!")
        break

winner()
