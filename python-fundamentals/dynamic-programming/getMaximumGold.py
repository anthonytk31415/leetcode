# getMaximumGold

# grid mxn 

# start from each position 
# map all possible routes 
# return max gold per cell
# return max gold across all starting cells


from math import inf

def getMaximumGold(grid):

    total_dist = set()       # house total distance of candidates; this step is prob not needed
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 0: 
                total_dist.add((i,j))

    # prevent the worst case scenario and just sum all of the entries
    if len(total_dist) == len(grid)*len(grid[0]): 
        return sum([sum(x) for x in grid])

    # iterate over each (i,j) candidate and instantiate
    # path will have current i,j in itself; dfs will simply find candidates, 
    # append path to result if there are no candidates (i.e. you arrived at a stopping point)
    def dfs(i, j, grid, x_res, path):
        candidates = []
        for (u,v) in [(i,j+1), (i,j-1), (i+1,j), (i-1,j)]:
            if 0 <= u < len(grid) and 0 <= v < len(grid[0]) and (u,v) not in path and grid[u][v] != 0: 
                candidates.append((u,v))
        if not candidates:
            x_res.append(path)
            return 
        else: 
            for (u,v) in candidates: 
                dfs(u,v,grid,x_res, path + [(u,v)])
        
    res = -inf                  # store max "dist" (i.e. path with max gold)
    for x in total_dist:        # do DFS on each candidate
        (i,j) = x
        x_res = []              # results for each x dfs will have an array of paths
        dfs(i, j, grid, x_res, [(i,j)])

        # calculate max gold of each element in the x_res
        x_max_dist = -inf
        for path in x_res: 
            cur_max = 0
            for step in path: 
                (u,v) = step
                cur_max += grid[u][v]
            if x_max_dist < cur_max: 
                x_max_dist = cur_max 
        if res < x_max_dist: 
            res = x_max_dist

    # there were no vaild paths
    if res == -inf:
        return 0

    return res

# grid = [[0,6,0],[5,8,7],[0,9,0]] # 24
# grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]] # 28

grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
print(getMaximumGold(grid))