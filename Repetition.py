# Function for choice of squares
# Function for translating squares into position in board
# Function to activate X or O player

square = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
square_taken = []

def choice():
    if choice in square_taken:
        print("This square is taken.")
        continue
    if choice in square:
        board[0][0] = player
        square_taken.append('1')
        print(board)
    elif choice == '2':
        board[0][1] = player
        square_taken.append('2')
        print(board)


def square():
    if square == '1':
        board[0][0]
    elif square == '2':
        board[0][1]
    elif square == '3':
        board[0][2]
    elif square == '4':
        board[1][0]
    elif square == '5':
        board[1][1]
    elif square == '6':
        board[1][2]
    elif square == '7':
        board[2][0]
    elif square == '8':
        board[2][1]
    elif square == '9':
        board[2][2]
