from collections import deque

def countSubIslands(grid1, grid2): 

    def determineIslands(grid):
        # build an array that contains for each island all the cells of that island
        visited = set()
        islands = []            # will contain the array with all islands
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                
                if (x,y) not in visited: 
                    visited.add((x,y))
                    if grid[x][y] == 1: 
                        curIsland = set()
                        queue = deque()
                        queue.append((x,y))
                        while queue: 
                            i,j = queue.popleft()
                            curIsland.add((i,j))
                            for (u, v) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:

                                if (0 <= u < len(grid) and 0 <= v < len(grid[0]) 
                                and (u,v) not in visited): 
                                    visited.add((u,v))
                                    if grid[u][v] == 1:
                                        queue.append((u,v))
                        
                        islands.append(curIsland)
        
        # now build the hash table
        cellToIslandMap = {}
        for idx, curIsland in enumerate(islands):
            for (i, j) in curIsland: 
                cellToIslandMap[(i,j)] = idx

        return [islands, cellToIslandMap]

    islands1, map1 = determineIslands(grid1)
    islands2, map2 = determineIslands(grid2)

    # print(islands1, islands2)
    # for each cell in each island in islandId2, ensure that each cell of that island
    # is in the same island in islandHash1
    res = 0

    for island in islands2: 
        cells2InSameIslandInGrid1 = True
        island1Idx = None
        
        for cell in island: 
            i,j = cell
            if (i,j) not in map1: 
                cells2InSameIslandInGrid1 = False
                break
            if island1Idx == None: 
                island1Idx = map1[(i,j)]
            else: 
                if island1Idx != map1[(i,j)]:
                    cells2InSameIslandInGrid1 = False
                    break
        
        if cells2InSameIslandInGrid1: res += 1
    # print(len(islands1), len(islands1))

    return res 

# grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
# grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]


# grid1 = [
#             [1,1,1,1,0,0],
#             [1,1,0,1,0,0],
#             [1,0,0,1,1,1],
#             [1,1,1,0,0,1],
#             [1,1,1,1,1,0],
#             [1,0,1,0,1,0],
#             [0,1,1,1,0,1],
#             [1,0,0,0,1,1],
#             [1,0,0,0,1,0],
#             [1,1,1,1,1,0]]

# grid2 = [
#             [1,1,1,1,0,1],
#             [0,0,1,0,1,0],
#             [1,1,1,1,1,1],
#             [0,1,1,1,1,1],
#             [1,1,1,0,1,0],
#             [0,1,1,1,1,1],
#             [1,1,0,1,1,1],
#             [1,0,0,1,0,1],
#             [1,1,1,1,1,1],
#             [1,0,0,1,0,0]]

grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]]
grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]

print(countSubIslands(grid1, grid2))
