# time: O(m*n)
# space: O(m*n)
# trick is union find with rank
# - to keep track of the largest set, rank will keep the size of the set
#       when it absorbs a new set through union, rank will increase by the rank 
#       of the absorbed element's set

def find(parent, x):
    (i,j) = x
    if parent[i][j] != (i,j):
        return find(parent, parent[i][j])
    else: 
        return (i, j) 

def union(parent, rank, p_x, p_y):
    (i,j) = p_x
    (u,v) = p_y
    if rank[i][j] < rank[u][v]: 
        parent[i][j] = p_y
        rank[u][v] += rank[i][j]
    elif rank[i][j] > rank[u][v]: 
        parent[u][v] = p_x
        rank[i][j] += rank[u][v]
    else: 
        parent[u][v] = p_x
        rank[i][j] += rank[u][v]

from math import inf

def maxAreaOfIsland(grid):
    # instantiate 
    parent = [[None for col in range(len(grid[0]))] for row in range(len(grid))]
    rank = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1: 
                parent[i][j] = (i,j)
                rank[i][j] = 1


    ## take all the ones, add them to a queue, then union-find all the neighbors with 1; 

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1: 
                for (u, v) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if (0 <= u < len(grid) and 0 <= v < len(grid[0]) 
                        and grid[u][v] == 1): 
                        p_x = find(parent, (i,j))
                        p_y = find(parent, (u,v))
                        if p_x != p_y: 
                            union(parent, rank, p_x, p_y)
                            print(parent)
    
    ## take the max rank
    # print('parent', parent)
    # print('rank', rank)
    return max([max(y) for y in rank])

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# grid = [[0,0,0,0,0,0,0,0]]
# grid = [[0,0,1],[1,1,1]]
print(maxAreaOfIsland(grid))