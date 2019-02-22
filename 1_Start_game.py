def start_game():
    start = input("Would you like to play tic tac toe? Choose 1 for yes\
 and 2 for no. ")
    try:
        while start != '1' and start != '2':
            print("This is not valid. Please enter 1 or 2.")
            start = input("Choose 1 for yes and 2 for no. ")
        else:
            if start == '1':
                print("Let's play!")

    except:
            print("Game over!")
            exit()
    print("Test")


start_game()
