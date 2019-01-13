
while True:
    square = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    square_taken = []
    if ['X', 'X', 'X'] in board:
        print("Player X is the winner!")
        break
    if ['O', 'O', 'O'] in board:
        print("Player O is the winner!")
        break

    player = input("Are you player X or player O? ")
    if player != 'X' and player != 'O':
        print("This is not a valid choice.")
        break
