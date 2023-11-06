def find(i, parent):
    if parent[i] == i: 
        return i
    else: 
        return find(parent[i], i)
    
def union(p_i, p_j, parent, rank):
    if rank[p_i] > rank[p_j]:
        parent[p_j] = p_i
        rank[p_i] += rank[p_j]
    else: 
        parent[p_i] = [p_j]
        rank[p_j] += rank[p_i]

def hasValidPath1(grid):
    parent = {}
    rank = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            parent[(i,j)] = (i,j)
            rank[(i,j)] = 1
    pass

# 1 = left or right
# 2 = up or down
# 3 = left or down
# 4 = right or down
# 5 = left or up
# 6 = right or up
roads = {
    1: ['l', 'r'],
    2: ['u', 'd'],
    3: ['l', 'd'],
    4: ['r', 'd'],
    5: ['l', 'u'],
    6: ['r', 'u']
}
# going right --> 1,3,5
# going left --> 1, 4, 6
# going up --> 2, 3, 4
# going down --> 2, 5, 6


def hasValidPath(grid):
    roads = {
        1: ['l', 'r'],
        2: ['u', 'd'],
        3: ['l', 'd'],
        4: ['r', 'd'],
        5: ['l', 'u'],
        6: ['r', 'u']
    }
    road_options  = {
        'r': set([1,3,5]), 
        'l': set([1,4,6]),
        'u': set([2, 3, 4]),
        'd': set([2, 5, 6]),
    }
    dir = {
        'r': (0,1), 
        'l': (0,-1),
        'u': (-1,0),
        'd': (1,0),
    }

    m, n = len(grid)-1, len(grid[0])-1
    visited = set()
    res = [False]
    def dfs(u, grid, visited, roads, road_options, m, n, res):
        print(u)
        visited.add(u)
        if u == (m, n):
            res[0] = True
            return
        i,j = u
        road = grid[i][j]
        for road_dir in roads[road]:
            coords = dir[road_dir]
            v = (i + coords[0], j + coords[1])
            a,b = v
            if v not in visited and 0 <= a <= m and 0 <= b <= n and grid[a][b] in road_options[road_dir]:
                dfs(v, grid, visited, roads, road_options, m, n, res)
    
    dfs((0,0), grid, visited, roads, road_options, m, n, res)
    return res[0]
    

# grid = [[4,1],[6,1]] # true
# grid = [[2,4,3],[6,5,2]] # true
# grid = [[1,2,1],[1,2,1]] # false
grid = [[1,1,2]]
# grid = [[1,1,1,1,1,1,3]] # true
print(hasValidPath(grid))







    