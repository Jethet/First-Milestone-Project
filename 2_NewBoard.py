"""
board = ['1 |', ' 2 |', ' 3\n',  '4 |', ' 5 |', ' 6\n',
        '7 |', ' 8 |', ' 9\n']
print(*board, sep='')
"""
from beautifultable import BeautifulTable
board = BeautifulTable()
board.append_row(['1', '2', '3'])
board.append_row(['4', '5', '6'])
board.append_row(['7', '8', '9'])
print(board)

new_table = board[:3]
print(new_table)
