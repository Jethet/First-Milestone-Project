# make a list of squares that can be chosen. Update list with choice of player
# so that squares that are taken are no longer on the available_square list.
"""
def open_square():
    available_square = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    player_choice = input("Where do you place your mark? ")
    try:
        if player_choice not in available_square:
            print("This is not a valid choice. ")
        else:
            available_square.remove(player_choice)
            return available_square
            return player_choice
        #player_choice = input("Where do you place your mark? ")
    except Exception as e:
        print("This is not a valid choice. ")

open_square()
"""

#TEST
def open_square():
    available_square = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    player_choice = input("Where do you place your mark? ")
    try:
        while player_choice not in available_square:
            print("This is not a valid choice. ")
            player_choice = input("Where do you place your mark? ")
        else:
            available_square.remove(player_choice)
            print(available_square)
            print(player_choice)
        #player_choice = input("Where do you place your mark? ")
    except ValueError:
        pass

open_square()
#
