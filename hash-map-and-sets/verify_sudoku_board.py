"""
Problem Statement -> Given a partially completed 9*9 Sudoku board, determine if the current state of the board adheres
to the rules of the game:

1. Each row and column must contain unique numbers between 1 and 9, or be empty (represented as 0).
2. Each of the nine 3*3 subgrids that compose the grid must contain unique numbers between 1 and 9, or be empty.
"""
from typing import  List
def verify_sudoku_board(board: List[List[int]]) -> bool:

    # create hash sets for each row, column, and subgrid to keep track of numbers previously seen num
    # on any rows, cols or subgrids
    row_sets = [set() for _ in range(9)]
    col_sets = [set() for _ in range(9)]
    subgrid_sets = [[set() for _ in range(3)] for _ in range(3)]
    
    for r in range(9):
        for c in range(9):
            num = board[r][c]
            # if num is 0 skip it don't add it to sets
            if num == 0:
                continue
            
            # check if num has been seen in current row, column or subgrid
            if num in row_sets[r]:
                return False
            if num in col_sets[c]:
                return False
            if num in subgrid_sets[r // 3][c // 3]:
                return False
            
            #if the num not seen then add it to corresponding to hash sets
            row_sets[r].add(num)
            col_sets[r].add(num)
            subgrid_sets[r // 3][c // 3].add(num)


board = [[3,0,6,0,5,8,4,0,0],
         [5,2,0,0,0,0,0,0,0],
         [0,8,7,0,0,0,0,3,1],
         [1,0,2,5,0,0,3,2,0],
         [9,0,0,8,6,3,0,0,5],
         [0,5,0,0,9,0,6,0,0],
         [0,3,0,0,0,8,2,5,0],
         [0,1,0,0,0,0,0,7,4],
         [0,0,5,2,0,6,0,0,0]]

print(verify_sudoku_board(board))
