# 2435. Paths in Matrix Whose Sum Is Divisible by K

# from collections import defaultdict

# use DP with memoization. You track the modulo paths at each step. and the recursive step is the top and the left of each cell's modulo + i,j's value then modulo

# Time: O(m*n); Space: O(m*n), tracking a constant modulo array of length k for each cell i, j 
# in this case, since k <= 50, we consider it constant throughout each iteration
# can optimize Space to O(m) since you only need the previous row

def numberOfPaths1(grid, k):

    dp = [[[] for _ in range(len(grid[0]))] for _ in range(len(grid))]
    dp[0][0] = [0]*k
    dp[0][0][grid[0][0] % k] = 1

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == j and i == 0: continue
            curMod = [0]*k
            for w in range(k):
                if i > 0:                 
                    curMod[(w + grid[i][j]) % k] += dp[i-1][j][w] 
                if j > 0: 
                    curMod[(w + grid[i][j]) % k] += dp[i][j-1][w] 

            dp[i][j] = curMod

    return dp[len(grid)-1][len(grid[0])-1][0] % (10**9 + 7)


# O(n) space build below

def numberOfPaths(grid, k):

    dpPrev = [[] for _ in range(len(grid[0]))]
    dpCur = [[0]*k for _ in range(len(grid[0]))]
    dpCur[0][grid[0][0] % k] = 1

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == 0 and j == 0: continue
            for w in range(k):
                if i > 0:                 
                    dpCur[j][(w + grid[i][j]) % k] += dpPrev[j][w] 
                if j > 0: 
                    dpCur[j][(w + grid[i][j]) % k] += dpCur[j-1][w] 

        dpPrev, dpCur = dpCur, [[0]*k for _ in range(len(grid[0]))]

    return dpPrev[-1][0] % (10**9 + 7)

grid = [[5,2,4],[3,0,5],[0,7,2]]
k = 3

# grid = [[7,3,4,9],[2,3,6,2],[2,3,7,0]]
# k = 1
print(numberOfPaths(grid, k))
    