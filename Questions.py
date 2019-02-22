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

To access the file I have  put
"""
with open('board', mode = 'rb') as handle:
    board = pickle.load(handle)
"""
after the function  choice(). For now, I have grayed this out as well.


Other question in general re. pickle: I know that the 'b' in 'wb' and 'rb'
stands for 'binary'. I also see code that just uses 'r' and 'w'.
Is there a best practice for this?
"""
