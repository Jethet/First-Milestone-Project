player = 'X' or 'O'
square = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] #3 x 3 squares on board
square_taken = ['1']
if player != 'X' and player != 'O':
    print("This is not a valid choice.")

game = True
while game == True:
    player = input("Are you player X or player O? ")
    choice = input("Where do you place your mark? ")
    if choice in square_taken:
        print("This square is taken.")
        continue
    else:
        game = False
