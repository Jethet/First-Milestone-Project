def start_game():
    while True:
        start = input("Would you like to play tic tac toe? Choose 1 for yes\
 and 2 for no. ")
        if start == '2':
            print("Game over.")
            return False
        elif start != '1' and start !='2':
            print("This is not valid. Please enter 1 or 2.")
        else:
            print("Player X starts the game.")
            break

start_game()
