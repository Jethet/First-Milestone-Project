
def repeat_game():
    answer = input("Would you like to play again? Choose 1 for yes\
    and 2 for no. ")
    while start != '1' and start != '2':
        print("This is not valid. Please enter 1 or 2.")
        start = input("Choose 1 for yes and 2 for no. ")
    else:
        if start == '1':
            print("Let's play!")
        elif start == '2':
            print("Thanks for player, until next time!")
            playing = False
            exit()
