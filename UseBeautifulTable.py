# The BeautifulTable module has been installed and can be imported:
from beautifultable import BeautifulTable

#CREATE TABLE by providing a name for the table and use BeautifulTable()
table = BeautifulTable()

#CREATE HEADERS: table.column_headers = ['name1', 'name2', 'name3']
#CREATE ROWS: table.append_row(['x', 'x', 'x']) NOTE: both ([])
#!!!!! HEADER DOES NOT COUNT AS A ROW !!!!!
table.column_headers = ['name1', 'name2', 'name3']
table.append_row(['1', '2', '3'])
table.append_row(['4', '5', '6'])
table.append_row(['7', '8', '9'])
print(table)

#CREATE new COLUMN: table.append_column('NAME'), ['DATA', 'D', 'D', 'D'])
#Watch out for the use of both () and []
table.append_column('player', ['X', 'O', 'X'])
print(table)

#You can also build a NEW TABLE using SLICING: the new table retains
#the properties of the original, it is a copy of the data.
new_table = table[:3]
print(new_table)

#!!!!! HEADER DOES NOT COUNT AS A ROW !!!!!
#You can ACCESS a ROW using its index:
print(list(table[1]))
#You can ACCESS a FIELD of a row via A) the index or B) the header
#A)
print(table[2][3])
#B)
print(table[1]['player'])

#You can ACCESS a COLUMN using header names (watch out for DUPLICATE
#HEADERS) or using index. The column returned is an iterator, not a list.
print(list(table['name3']))

#INSERTING rows and columns:
table.insert_row(3, ['10', '11', '12', 'O'])
table.insert_column(0, 'letter', ['a', 'b', 'c', 'd'])
print(table)

#DELETING rows and columns: just use del
#You can also use METHODS: pop_row, pop_column, using index
#In addition, you can use pop_column('NAME COLUMN') to delete column
del table[0]
print(table)
del table['player']
print(table)

#UPDATING data in a table: use SLICING
table[1][0] = 'x'
print(table)
table[1]['letter'] = 'z'  #does the same thing
print(table)

#You can customize the look of the table:
#alignment of colums with
table.column_alignments['name1'] = BeautifulTable.ALIGN_LEFT
table.column_alignments['name3'] = BeautifulTable.ALIGN_RIGHT
print(table)

"""
Other options are:
- updating existing columns with: table['NAME COLUMN'] = ['a', 'b', 'c']
- use methods update_row and update_column to perform same operations
- use append_column or insert_column to create new columns
- you can SEARCH for rows or headers:
'xxx' in table (returns True or False)   or
['x', 'y', 'z'] in table   (returns True or False)
- sort table based on a column specifying index or header:
table.sort('NAME COLUMN')

"""
