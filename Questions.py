"""
Questions for David:

I added:
"""
with open('board', mode = 'wb') as handle:  #this saves the board
    pickle.dump(board, my_file)
"""
after the function new_board() in main() because in my thinking the board file
is created in the function new_board() and should be saved as a file to use in
the rest of the programme.

To access the file I have now put
"""
with open('board', mode = 'rb') as handle:
    board = pickle.load(handle)
"""
after the function  choice().


Other question in general re. pickle: I know that the 'b' in 'wb' and 'rb'
stands for 'binary'. I also see code that just uses 'r' and 'w'.
Is there a best practice for this?
"""
