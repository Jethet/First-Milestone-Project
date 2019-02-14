# The game has two players and they have to choose if they want to play.
# The players also have to choose X or O as their mark.
# This function is part of main()

def player():
    while True:
        player = input("Are you player X or player O? ")
        if player != 'X' and player != 'O':
            print("This is not a valid choice. Choose X or O. ")
        else:
            print("You will be player", player, "for this game.")
            break


player()
