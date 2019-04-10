"""
Questions for David:

I added:
"""
with open('board', mode = 'wb') as handle:  #this saves the board
    pickle.dump(board, my_file)
"""
after the function new_board() in main() because in my thinking the board file
is created in the function new_board() and should be saved as a file to use in
the rest of the programme. ERROR: name 'board' is not defined.
I do not understand this because the board is defined in the function new_board()
and returned. For now, I have grayed it out.

To access the file I have put
"""
with open('board', mode = 'rb') as handle:
    board = pickle.load(handle)
"""
after the function  choice(). For now, I have grayed this out as well.
I have also again use 'pickle.dump' at the end of main() to save the new_board
after running the programme but that seems too much? It is now grayed out.

Other question in general re. pickle: I know that the 'b' in 'wb' and 'rb'
stands for 'binary'. I also see code that just uses 'r' and 'w'.
Is there a best practice for this?


Next question: how to repeat the game? I wrote a function but there are problems with it:

-  when repeating the game, the new list of numbers is not used and the
   programme continues to use the previous list, i.e. with the numbers that
   are left from the previous game;

-  in some cases, after only one or two choices, the programme already declares
   a winner; it seems the choices of the previous game are still used even
   though the list of available squares is renewed and the board is new;

-  the programme also declares a winner when 3 in a row is X X O;

-  HOW TO REPEAT GAME WITHOUT FUNCTIONS start_game() AND new_board()?

-  should pickle/unpickle be used? when and how?


"""
