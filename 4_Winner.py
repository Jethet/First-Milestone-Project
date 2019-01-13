# This function returns a 'winner!' message if a player has won the game.
# There are many options for getting three in a row: horizontal,
# vertical or diagonal.
# This function is part of main()

def winner():
    # For horizontal three in a row:
    if ['X', 'X', 'X'] in board:
        print("Player X is the winner!")
        break
    if ['O', 'O', 'O'] in board:
        print("Player O is the winner!")
        break

    for player == 'X' or player == 'O':
        # Two options diagonal three in a row:
        if board[0][0] and board[1][1] == board[2][2] or
            board[0][2] and board[1][1] == board[2][0]:
            if player == 'X':
                print("Player X is the winner!")
            elif player == 'O':
                print("Player O is the winner!")
        elif board[0][0] and board[0][1] == board[0][2] or
              board[1][0] and board[1][1] == board[1][2] or
               board[2][0] and board[2][1] == board[2][2]:
               if player == 'X':
                   print("Player X is the winner!")
               elif player == 'O':
                   print("Player O is the winner!")



            print(player, " is the winner!")
            break
        elif board[0][2] and board[1][1] == board[2][0]:
            print(player, " is the winner!")
            break
        # Three options vertical three in a row:
        if board[0][0] and board[1][0] == board[2][0]:
            print(player, " is the winner!")
            break
        elif board[0][1] and board[1][1] == board[2][1]:
            print(player, " is the winner!")
            break
        elif board[0][2] and board[1][2] == board[2][2]:
            print(player, " is the winner!")
            break

winner()
