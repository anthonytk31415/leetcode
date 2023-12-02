from math import sqrt

# Time: O(mn)
# Space: saving O(n) approach for n columns. We do DP, we iterate across rows, 
# and we only need the previous and current row records. 

# Intuition: for an i, j where matrix[i][j] ==1, we can form the largest square by taking the 
# min of {side of squares from (i-1, j), (i-1, j-1), (i, j-1)} + 1.

def maximalSquare(matrix):
    matrix = [[int(x) for x in row] for row in matrix]
    prevDp = [x for x in matrix[0]]
    curDp = [0] * len(matrix[0])
    maxSquare = 0
    for row in range(len(matrix)):
        for col in range(len(curDp)):
            if row == 0 or col == 0: 
                curDp[col] = matrix[row][col]
            else: 
                if matrix[row][col] >0: 
                    curDp[col] = min(curDp[col - 1], prevDp[col], prevDp[col - 1]) + 1                
            maxSquare = max(maxSquare, int(curDp[col]**2))
        prevDp, curDp  = [x for x in curDp], [0] * len(matrix[0])
    return maxSquare

# matrix = [["0","1"],["1","0"]]
# matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

matrix = [["1"]]
# matrix = [["0","0","0","1"],
#           ["1","1","0","1"],
#           ["1","1","1","1"],
#           ["0","1","1","1"],
#           ["0","1","1","1"]]


print(maximalSquare(matrix))