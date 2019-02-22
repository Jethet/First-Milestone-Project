def start_game():
    def start_game():
        start = input("Would you like to play tic tac toe? Choose 1 for yes\
     and 2 for no. ")
        while start != '1' and start != '2':
            print("This is not valid. Please enter 1 or 2.")
            if start == '1':
                print("Let's play!")
        # The EXIT() function is needed to stop the entire programme from
        # running if the player chooses 2: stop playing TTT
        else:
            exit()
