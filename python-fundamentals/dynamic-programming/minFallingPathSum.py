

# You need only prev and cur; here we use the existing matrix so space is 
# O(1); need to iterate across rows and cols so Time = O(mn)

# Trivial: 1 row; take min of the row

# given i row, j column, min to get to i, j is the matrix[i][j] + (1) where 
# (1) = min{possible way to get there} = min{dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1]}

# at the end, take the min of row[-1]


def minFallingPathSum(matrix):

    for i in range(1, len(matrix)):
        for j in range(len(matrix[0])):
            jOptions = []
            for u in [j, j-1, j+1]:
                if 0 <= u < len(matrix[0]):
                    jOptions.append(matrix[i-1][u])
            matrix[i][j] = min(jOptions) + matrix[i][j]

    return min(matrix[-1])

# matrix = [[-19,57],[-40,-5]]
matrix = [[2,1,3],[6,5,4],[7,8,9]]

print(minFallingPathSum(matrix))