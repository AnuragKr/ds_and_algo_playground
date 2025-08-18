"""
Problem Statement -> Write a function that takes in an n*m two dimensional array
and returns a one-dimensional array of all the array's elements in
spiral order.
i/p -> array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
o/p -> array = [
       [1,2,3,4],
       [12,13,14,5],
       [11,16,15,6],
       [10,9,8,7]
       ]
"""

"""
Pattern -> Math & Geometery
"""
def spiral_traverse(array):
    #Initialization
    start_row,end_row = 0,len(array)-1
    start_col,end_col = 0,len(array[0])-1
    result = []

    while start_col <= end_col and start_row <= end_row:
        #Top side of matrix
        for idx in range(start_col,end_col+1):
            result.append(array[start_row][idx])
        #Right side of matrix
        for idx in range(start_row+1,end_row+1):
            result.append(array[idx][end_col])
        #Botton Side of matrix
        for idx in reversed(range(start_col,end_col)):
            #Handling edge case when there will be one row which 
            # will be counted twice
            if start_row == end_row:
                break
            result.append(array[end_row][idx])
        #Left side of array
        for idx in reversed(range(start_row+1,end_row)):
            #Handling edge case when there will be single col which 
            # will be counted twice
            if start_col == end_col:
                break
            result.append(array[idx][start_col])
        
        start_row += 1
        end_row -= 1
        start_col += 1
        end_col -= 1
    
    return result

array = [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]
#array = [[1,2,3,4]]
#array = [[1],[12],[11],[10]]
print(spiral_traverse(array))