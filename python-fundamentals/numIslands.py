#number of islands
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def neighbors(i,j, m,n):
            matrix = [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]
            return list(filter(lambda x: x[0] <m and x[0]>=0 and x[1] <n and x[1] >=0, matrix))
        def islandCheck(grid, i, j, m, n, checked):
            if (i,j) not in checked: ## do if entry has not been checked
                checked[(i,j)] = 1
                cur = grid[i][j]
                if cur =='1':
                    checkNeighbors = neighbors(i,j,m,n)
                    for x in checkNeighbors:
                        a, b = x[0], x[1]
                        if (a,b) not in checked: ## do if entry has not been checked
                            islandCheck(grid, a, b, m, n, checked)

        islandCounter = 0
        m = len(grid)       ## num rows
        n = len(grid[0])    ## num columns
        checked = {}     # this has length m * n; 1 indicates we've checked the entry in the matrix

        for i in range(0,m):
            for j in range(0,n):
                if (i,j) not in checked: ## do if entry has not been checked
                    if grid[i][j] == '1':
                        islandCheck(grid, i,j,m,n, checked)
                        islandCounter +=1
        return islandCounter

grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
z = Solution.numIslands('b',grid2)
print(f'output of solution is: {z}')