# choice is translated into board_coordinates:
#  board_coordinates = transform_choice(choice)

def transform_choice(player_choice):
    board_squares = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1.0), 5:(1,1), 6:(1,2),\
                          7:(2,0), 8:(2,1), 9:(2,2)}
    board_coordinates = board_squares.get(player_choice)
    return board_coordinates

print(transform_choice(9))
print(transform_choice(5))
