# This function returns a 'winner!' message if a player has won the game.
# Two diagonal, three horizontal and three vertical options to win.
# This function is part of main()

def winner():
    player = 'X' or 'O'
    if board[0][0] and board[1][1] == board[2][2] or board[0][2] and \
          board[1][1] == board[2][0] or board[0][0] and board[0][1] == \
          board[0][2] or board[1][0] and board[1][1] == board[1][2] or \
          board[2][0] and board[2][1] == board[2][2] or board[0][0] and \
          board[1][0] == board[2][0] or board[0][1] and board[1][1] \
          == board[2][1] or board[0][2] and board[1][2] == board[2][2] \
          and player == 'X':
        print("Player X is the winner!")
        break
    elif board[0][0] and board[1][1] == board[2][2] or board[0][2] and \
          board[1][1] == board[2][0] or board[0][0] and board[0][1] == \
          board[0][2] or board[1][0] and board[1][1] == board[1][2] or \
          board[2][0] and board[2][1] == board[2][2] or board[0][0] and \
          board[1][0] == board[2][0] or board[0][1] and board[1][1] \
          == board[2][1] or board[0][2] and board[1][2] == board[2][2] \
          and player == 'O':
        print("Player O is the winner!")
        break

winner()
