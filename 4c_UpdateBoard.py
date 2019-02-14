# After player_choice is made and transformed into board_coordinates,
# show choice on the board. Adapt board with player_choice on relevant square
# arguments for the function are: board, player, board_coordinates

def update_board():
    from beautifultable import BeautifulTable
    board = BeautifulTable()
    board.append_row(['1', '2', '3'])
    board.append_row(['4', '5', '6'])
    board.append_row(['7', '8', '9'])

    #THIS CODE IS ADDED FOR TESTING, SHOULD BE ONLY player = player()
    while True:
        player = input("Are you player X or player O? ")
    #return player
        while player != 'X' and player != 'O':
            print("This is not a valid choice. ")
            player = input("Are you player X or player O? ")
        #return player_choice
        player_choice = int(input("Where do you place your mark? "))
        available_square = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        while player_choice not in available_square:
            print("This is not a valid choice. ")
            player_choice = int(input("Where do you place your mark? "))


        #This is the actual code to update the board:
        board_squares = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2),\
                              7:(2,0), 8:(2,1), 9:(2,2)}
        board_coordinates = board_squares.get(player_choice)

        if board_coordinates == (0,0):
            board[0][0] = player
            print(board)
        elif board_coordinates == (0,1):
            board[0][1] = player
            print(board)
        elif board_coordinates == (0,2):
            board[0][2] = player
            print(board)
        elif board_coordinates == (1,0):
            board[1][0] = player
            print(board)
        elif board_coordinates == (1,1):
            board[1][1] = player
            print(board)
        elif board_coordinates == (1,2):
            board[1][2] = player
            print(board)
        elif board_coordinates == (2,0):
            board[2][0] = player
            print(board)
        elif board_coordinates == (2,1):
            board[2][1] = player
            print(board)
        elif board_coordinates == (2,2):
            board[2][2] = player
            print(board)
        else:
            print("This is not a valid choice.")
    return False


update_board()