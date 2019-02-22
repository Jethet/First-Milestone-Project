def start_game():
    start = input("Would you like to play tic tac toe? Choose 1 for yes\
 and 2 for no. ")
    while start != '1' and start != '2':
        print("This is not valid. Please enter 1 or 2.")
    else:
        if start == '2':
            print("Game over!")
            exit()
        elif start == '1':
            print("Let's play!")

start_game()
