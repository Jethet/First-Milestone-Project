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
    player = input("Are you player X or player O? ")
    #return player
    while player != 'X' and player != 'O':
        print("This is not a valid choice. ")
        player = input("Are you player X or player O? ")
    #return player
    player_choice = input("Where do you place your mark? ")
    #return player_choice
    #THIS CODE IS ADDED FOR TESTING, SHOULD BE ONLY board_coordinates()
    board_squares = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2),\
                          7:(2,0), 8:(2,1), 9:(2,2)}
    board_coordinates = board_squares.get(player_choice)
    return board_coordinates
    print(board_coordinates)

    #This is the actual code to update the board:
    if board_coordinates == (0,0) and player == 'X':
        board[0][0] == 'X'
        print(board)
    elif board_coordinates == (0,1) and player == 'X':
        board[0][1] = 'X'
        print(board)
    elif board_coordinates == (0,2) and player == 'X':
        board[0][2] = 'X'
        print(board)
    elif board_coordinates == (1,0) and player == 'X':
        board[1][0] = 'X'
        print(board)
    elif board_coordinates == (1,1) and player == 'X':
        board[1][1] = 'X'
        print(board)
    elif board_coordinates == (1,2) and player == 'X':
        board[1][2] = 'X'
        print(board)
    elif board_coordinates == (2,0) and player == 'X':
        board[2][0] = 'X'
        print(board)
    elif board_coordinates == (2,1) and player == 'X':
        board[2][1] = 'X'
        print(board)
    elif board_coordinates == (2,2) and player == 'X':
        board[2][2] = 'X'
        print(board)

    return board

print(update_board())
