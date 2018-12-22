
from itertools import cycle

def alternate():
    turn = True
    winner = 'XXX' or 'OOO'
    currentSymbol = 'X'

    while not winner:
        if currentSymbol == 'X': currentSymbol = 'O'
        elif currentSymbol == 'O': currentSymbol = 'X'




alternate()



"""
def alternate():
    player = int(input("Choose betweeen 1 and 2. "))
    while True:
        if player == 1:
            print("Great")
        if player == 2:
            print("Fine")
        else:
            print("This is not a valid choice.")
        break
"""
