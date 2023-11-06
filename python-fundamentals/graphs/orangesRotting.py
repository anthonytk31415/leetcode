from collections import defaultdict

def orangesRotting(grid): 
    # store tuples to keep track of infected 
    hasInfected, justRot, nextTurnWillRot = set(), set(), set()        
    allOranges = set([(i,j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] !=0])
    # instantiate: gather all infected oranges
    for i in range(len(grid)): 
        for j in range(len(grid[0])):
            if grid[i][j] == 2: 
                hasInfected.add((i,j))
                justRot.add((i,j))
                # for each infected orange, put in nextTurnWillRot
                for a,b in [(-1,0), (1, 0), (0,-1), (0,1)]:
                    if 0 <= i + a <= len(grid)-1 and 0 <= j + b <= len(grid[0])-1 and grid[i+a][j+b] == 1 and (i+a,j+b) not in hasInfected:
                        nextTurnWillRot.add((i+a, j+b))
    counter = 0 
    while nextTurnWillRot:
        counter += 1
        justRot = nextTurnWillRot
        for x in justRot:
            hasInfected.add(x)
        nextTurnWillRot = set()
        for i,j in justRot: 
            for a,b in [(-1,0), (1, 0), (0,-1), (0,1)]:
                if 0 <= i + a <= len(grid)-1 and 0 <= j + b <= len(grid[0])-1 and grid[i+a][j+b] == 1 and (i+a,j+b) not in hasInfected:
                    nextTurnWillRot.add((i+a, j+b))
    if hasInfected == allOranges:
        return counter
    else:
        return -1
    print(justRot)

# grid = [[2,1,1],[1,1,0],[0,1,1]]
# grid = [[2,1,1],[0,1,1],[1,0,1]]
grid = [[0,2]]
print(orangesRotting(grid))


### try rewriting this in a queue using BFS

