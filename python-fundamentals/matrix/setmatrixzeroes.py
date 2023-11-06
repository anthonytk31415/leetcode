# Set Matrix Zeroes

# 8:19

# m x n matrix

# queue first, collect all the 0's 
# then replace the 0s 

# Time: O(n*m)
# Space: O(n+m)
# can reduce to O(1) if you want to do more iterations to replace to zeroes

from collections import deque

def setZeroes(matrix):
    rowvisited = set()
    colvisited = set()

    row_queue = deque()
    col_queue = deque()

    for i in range(len(matrix)):        #rows
        for j in range(len(matrix[0])): #cols
            if matrix[i][j] == 0: 
                row_queue.append(i)
                col_queue.append(j)
    
    while row_queue: 
        cur_row = row_queue.popleft()
        if cur_row not in rowvisited: 
            rowvisited.add(cur_row)
            matrix[cur_row] = [0] * len(matrix[0])

    while col_queue: 
        cur_col = col_queue.popleft()
        if cur_col not in colvisited: 
            colvisited.add(cur_col)
            for row in range(len(matrix)):
                matrix[row][cur_col] = 0

    return matrix

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

setZeroes(matrix)
print(matrix)
