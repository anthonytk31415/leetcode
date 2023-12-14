def onesMinusZeros(grid):
    res = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    m = len(grid)
    n = len(grid[0])
    for i in range(len(grid)):
        sumGridRow = sum(grid[i])
        rowSum = sumGridRow - (m - sumGridRow) 
        for j in range(len(grid[0])):
            res[i][j] = rowSum
    
    # print(res)
    for j in range(len(grid[0])):
        sumGridCol = sum([grid[i][j] for i in range(len(grid))])
        colSum = sumGridCol - (n - sumGridCol)      # 1 - (3 - 1) = 1-2 = -1
        for i in range(len(grid)):
            res[i][j] = res[i][j] + colSum
    
    return res

grid = [[0,1,1],[1,0,1],[0,0,1]]
print(onesMinusZeros(grid))