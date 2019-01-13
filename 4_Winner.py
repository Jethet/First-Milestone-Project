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
        if choice[0][0] and choice[1][1] == choice[2][2]:
            print(player, " is the winner!")
            break
        elif choice[0][2] and choice[1][1] == choice[2][0]:
            print(player, " is the winner!")
            break
        # Three options vertical three in a row:
        if choice[0][0] and choice[1][0] == choice[2][0]:
            print(player, " is the winner!")
            break
        elif choice[0][1] and choice[1][1] == choice[2][1]:
            print(player, " is the winner!")
            break
        elif choice[0][2] and choice[1][2] == choice[2][2]:
            print(player, " is the winner!")
            break

winner()
