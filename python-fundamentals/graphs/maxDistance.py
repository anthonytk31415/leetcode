from collections import deque

# queue and bfs
# O(mn) time, O(mn) space for the queue and for the visited set

def maxDistance(grid):
    queue = deque()
    visited = set()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1: 
                queue.append((i, j, 0))
                visited.add((i, j))
    
    if not queue or len(queue) == len(grid)*len(grid[0]): return -1

    maxDist = -1
    while queue: 
        for _ in range(len(queue)):
            i, j, dist = queue.popleft()
            maxDist = max(maxDist, dist)
            for u, v in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= u < len(grid) and 0 <= v < len(grid[0]) and (u, v) not in visited: 
                    visited.add((u, v))
                    queue.append((u, v, dist + 1))
    return maxDist
    # if max dist = 0 then there's no water, so return -1

grid = [[1,0,1],[0,0,0],[1,0,1]]
grid = [[1,0,0],[0,0,0],[0,0,0]]
grid = [[1,1,1], [1,1,1]]
grid = [[0,0,0,0], [0,0,0,0],[0,0,0,0],[0,0,0,0]]
grid = [[0,1,0,0], [0,0,0,0],[0,0,1,0],[0,0,0,0]]
# grid = [[0,0,0,0], [0,0,0,0],[0,0,0,0],[0,0,0,0]]
print(maxDistance(grid))