from heapq import heappush, heappop

def shortestPathBinaryMatrix(grid):
    if grid[0][0] == 1: return -1

    n = len(grid)
    queue = []
    heappush(queue, (1, (0,0)))
    visited = set()
    visited.add((0,0))

    while queue: 
        dist, coords = heappop(queue)
        u, v = coords
        if coords == (n-1, n-1): 
            return dist
        for i, j in [(u-1,v),(u+1,v),(u,v-1),(u,v+1),(u-1,v-1),(u+1,v+1),(u+1,v-1),(u-1,v+1)]:
            if 0 <= i < n and 0 <= j < n and (i,j) not in visited and grid[i][j] == 0:
                heappush(queue, (dist + 1, (i,j)))
        
    return -1

# grid = [[0,0,0],[1,1,0],[1,1,0]]
# grid = [[0,1],[1,0]]
grid = [[0,0,0],[1,1,0],[1,1,0]]
print(shortestPathBinaryMatrix(grid))

