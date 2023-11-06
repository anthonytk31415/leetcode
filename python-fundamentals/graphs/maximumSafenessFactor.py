from heapq import heappush, heappop
from math import inf 

# time: O(nmlog(nm))
# space: O(nm)
def maximumSafenessFactor(grid):

    queue = []
    visited = set()
    safeGrid = [ [inf for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1: 
                heappush(queue, (0, (i,j)))
                safeGrid[i][j] = 0
                visited.add((i,j))

    while queue: 
        safeVal, (i, j) = heappop(queue)
        for u, v in [(i -1, j), (i + 1, j), (i, j+1), (i, j-1)]:
            if 0 <= u < len(grid) and 0 <= v < len(grid[0]) and safeGrid[u][v] not in visited and 1 + safeVal < safeGrid[u][v]:
                safeGrid[u][v] = safeVal + 1
                heappush(queue, (safeVal + 1, (u, v)))
                visited.add((u,v))                

    # now get to the end
    queue = [(-safeGrid[0][0], (0,0))]
    
    currentSafe = [[-inf for _ in range(len(grid[0]))] for _ in range(len(grid))]
    currentSafe[0][0] = -safeGrid[0][0]
    visited = set()
    # print(currentSafe)
    # print(safeGrid)
    while queue: 
        safeVal, (i, j) = heappop(queue)

        visited.add((i,j))

        if (i,j) == (len(grid)-1, len(grid[0])-1 ):
            return -safeVal
        
        for u, v in [(i -1, j), (i + 1, j), (i, j+1), (i, j-1)]:
            if 0 <= u < len(grid) and 0 <= v < len(grid[0]) and (u,v) not in visited:
                newSafeVal = max(safeVal, -safeGrid[u][v])
                if currentSafe[u][v] < newSafeVal:
                    heappush(queue, (newSafeVal, (u,v)))
                    currentSafe[u][v] = newSafeVal

grid = [    
    [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

# grid = [[1,1],[1,1]]

# grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]

# grid = [[1,0,0],[0,0,0],[0,0,1]]
# Output: 0
grid = [[0,0,1],[0,0,0],[0,0,0]]

print(maximumSafenessFactor(grid))