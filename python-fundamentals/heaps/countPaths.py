# https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/?envType=daily-question&envId=2023-11-06

from heapq import heappush, heappop

def countPaths(grid):
    queue = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            heappush(queue, (-grid[i][j], i, j))

    numPaths = [[1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    # print(numPaths)

    while queue: 
        _, i, j = heappop(queue)
        curVal = grid[i][j]
        for u, v in [(i + 1, j), (i - 1,j), (i, j + 1), (i, j - 1)]:
            if 0 <= u < len(grid) and 0 <= v < len(grid[0]):
                nextVal = grid[u][v]
                if curVal < nextVal:
                    numPaths[i][j] += numPaths[u][v] 

    
    return sum([sum(x) for x in numPaths])



grid = [[1,1],[3,4]]
print(countPaths(grid))