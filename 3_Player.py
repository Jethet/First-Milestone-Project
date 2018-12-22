#The game has two players and they have to choose if they play as X or O
#Player 1 will play with X and player 2 plays with O. Player 1 can start.

def player():
    start = input("Would you like to play tic tac toe? Choose 1 for yes and 2 for no. ")
    if start == '2':
        print("Game over.")
    elif start != '1' and start !='2':
        print("This is not a valid entry.")
    else:
        player = input("Choose which player you want to be: 1 for 'X' and 2 for '0'. ")
        if player == '1':
            print("Player 1 will start: you can choose first.")
        elif player == '2':
            print("You are player 2. Player 1 gets the first turn.")
        else:
            print("This is not a valid entry.")


player()
