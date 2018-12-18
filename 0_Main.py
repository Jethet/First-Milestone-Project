"""
TicTacToe: 2 players should be able to play the game (both sitting at
the same computer).
The board should be printed out every time a player makes a move.
You should be able to accept input of the player position and then
place a symbol on the board.
"""

#First step is ask player to play and what choice (X or O)
#Player is identified as player 1 or player 2; player 1 starts.
player()

#If the player wants to play: show board and explain choices
new_board()

#If player chooses a square, the choice is shown on the board
choice()

#To clear screen between games:
print(\n*100)
