# https://leetcode.com/problems/rotate-image/

## create new matrix
## then enter in the old matrix the new values
# time: O(N^2)
# Space: O(N^2)

def rotate(matrix):
    n = len(matrix)
    new_matrix = [[None for col in range(n)] for row in range(n)]
    for u in range(len(matrix)):
        for v in range(len(matrix[0])):
            matrix[u][v] = new_matrix[v][n-1-u]
    
    for u in range(len(matrix)):
        for v in range(len(matrix[0])):
            matrix[u][v] = new_matrix[u][v]


