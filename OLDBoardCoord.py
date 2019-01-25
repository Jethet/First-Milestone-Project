# This is the extended version, to be able to run for testing

def board_coordinates(choice):
    
    # This is only needed to test the function but should not be in main()
    board = BeautifulTable()
    board.append_row(['1', '2', '3'])
    board.append_row(['4', '5', '6'])
    board.append_row(['7', '8', '9'])
    print(board)
    with open('board', mode = 'wb') as my_file:  #this is meant to save the board
        pickle.dump(board, my_file)
        while True:
            player = input("Are you player X or player O? ")
            if player != 'X' and player != 'O':
                print("This is not a valid choice.")
                break
            choice = input("Where do you place your mark? ")

            # This is where the function begins:
            if choice == '1':
                square_taken.append('1')
                #print(square_taken)
                return (0,0)
            elif choice == '2':
                square_taken.append('2')
                #print(square_taken)
                return (0,1)
            elif choice == '3':
                square_taken.append('3')
                return (0,2)
            elif choice == '4':
                square_taken.append('4')
                return (1,0)
            elif choice == '5':
                square_taken.append('5')
                return (1,1)
            elif choice == '6':
                square_taken.append('6')
                return (1,2)
            elif choice == '7':
                square_taken.append('7')
                return (2,0)
            elif choice == '8':
                square_taken.append('8')
                return (2,1)
            elif choice == '9':
                square_taken.append('9')
                return (2,2)

first_element, second_element = board_coordinates('1')
print(first_element, second_element)

board_coordinates(square)
