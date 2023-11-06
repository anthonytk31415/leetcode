# unique path 2
# https://leetcode.com/problems/unique-paths-ii/description/

# the DP step: the the number of paths at the current step = sum of number of paths in the prev steps 
# time: O(m*n); run through each of the cells in the matrix
# space: O(m*n) keep track of the entries in each cell

def uniquePathsWithObstacles(obstacleGrid):
    cache = {}
    m = len(obstacleGrid)           # rows
    n = len(obstacleGrid[0])        # cols

    def helper(grid, m, n, cache):
        if (m,n) in cache: 
            return cache[(m,n)]
        elif m< 0 or n < 0 or grid[m][n] == 1: 
            return 0
        elif m==0 and n == 0: 
            return 1
        else: 
            cache[(m,n)] = helper(grid, m, n-1, cache) + helper(grid, m-1, n, cache)
            return cache[(m,n)]
    
    return helper(obstacleGrid, m-1, n-1, cache)