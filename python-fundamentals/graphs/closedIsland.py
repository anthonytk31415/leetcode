# iterate across each i,j pair. 
# - if its visited, continue. 
# - if it's a 0, dfs and continue for each neighbor if it is within boundaries. 
#     - if you ever hit a wall, this continuous set of 0s cannot be a an island 
#     - if at the end your wall indicator is false, add one and move on 

# Time and Space O(m*n) for m rows, n columns

def closedIsland(grid):
    visited = set()         # throw i and j's in here. 

    def dfs(i, j, dfsWall): 
        visited.add((i,j))
        if grid[i][j] == 0: 
            for u,v in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if not (0 <= u < len(grid) and 0 <= v < len(grid[0])):
                    dfsWall[0] = True
                elif (u,v) not in visited:   # youre within boundaries
                    dfs(u, v, dfsWall)
    
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i,j) not in visited:
                if grid[i][j] == 1: 
                    visited.add((i,j))
                elif grid[i][j] == 0: 
                    dfsWall = [False]
                    dfs(i,j, dfsWall)
                    if dfsWall[0] == False: 
                        res +=1
    return res

# grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
# grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
grid = [[1,1,1,1,1,1,1],
        [1,0,0,0,0,0,1],
        [1,0,1,1,1,0,1],
        [1,0,1,0,1,0,1],
        [1,0,1,1,1,0,1],
        [1,0,0,0,0,0,1],
        [1,1,1,1,1,1,1]]

print(closedIsland(grid))