# The game has two players and they have to choose if they want to play as X or O
# The players also have to choose X or O as their mark

def player():
    start = input("Would you like to play tic tac toe? Choose 1 for yes and 2 for no. ")
    if start == '2':
        print("Game over.")
        return
    elif start != '1' and start !='2':
        print("This is not valid. Please enter 1 or 2.")
        return
    else:
        print("Player X starts the game.")
    player = input("Are you player X or player O? ")
    if player != 'X' and player != 'O':
        print("This is not a valid choice.")
        break


player()
