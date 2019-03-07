# This function returns a 'winner!' message if a player has won the game.
# Two diagonal, three horizontal and three vertical options to win.
# This function is part of main()

def check_winner(board):
    if board[0][0] and board[1][1] and board[2][2] == 'X' or board[0][2] and \
       board[1][1] and board[2][0] == 'X' or board[0][0] and board[0][1] and \
       board[0][2] == 'X' or board[1][0] and board[1][1] and board[1][2] == 'X' \
       or board[2][0] and board[2][1] and board[2][2] == 'X' or board[0][0] and \
       board[1][0] and board[2][0] == 'X' or board[0][1] and board[1][1] \
       and board[2][1] == 'X' or board[0][2] and board[1][2] and board[2][2] \
       == 'X' or board[0][0] and board[1][1] and board[2][2] == 'O':
        print("We have a winner!")
        return True
    else:
        print("No winner!")
        return False
