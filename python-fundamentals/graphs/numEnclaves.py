


def numEnclaves(grid):
    visited = set()
    res = 0

    def dfs(row, col, border, grid, visited): 
        visited.add((row, col))
        for x in [[row - 1, col], [row +1, col], [row, col - 1], [row, col+1]]:
            i,j = x
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                border[0] = True
        print(border[0], row, col)
        dfs_res = 0
        for v in [[row - 1, col], [row +1, col], [row, col - 1], [row, col+1]]:
            i,j = v
            if (i,j) not in visited and i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] == 1:
                dfs_res += dfs(i, j, border, grid, visited)
        return 1 + dfs_res

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) not in visited:
                if grid[row][col] == 1:  
                    border = [False]
                    count = dfs(row, col, border, grid, visited)
                    if border[0] == False: 
                        res += count
                else: 
                    visited.add((row, col))
    
    return res

grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
print(numEnclaves(grid))