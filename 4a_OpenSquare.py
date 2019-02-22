# make a list of squares that can be chosen. Update list with choice of player
# so that squares that are taken are no longer on the available_square list.

def open_square():
    player_choice = input("Where do you place your mark? ")
    available_square = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    while player_choice not in available_square:
        print("This is not a valid choice. ")
        player_choice = input("Where do you place your mark? ")

    available_square.remove(player_choice)
    return available_square


print(open_square())
