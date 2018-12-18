#This is the function that asks the player to choose where to tic
#and also checks if choice is valid

def choice_board():
    square = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    choice = int(input("Which square do you choose? "))
    if choice in square:
        board = ['1 |', ' 2 |', ' 3\n',  '4 |', ' 5 |', ' 6\n',
                '7 |', ' 8 |', ' 9\n']
        choice = choice - 1
        board[choice] = 'X |'
        print(*board, sep='')
        return board
    else:
        print("This is not a valid choice.")

choice_board()
