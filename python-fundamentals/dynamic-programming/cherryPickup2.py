from math import inf

# Decently tricky DP problem because you have to keep track of 2 paths at once. 
# Suppose DP = max path with ending vertex u, v on ith iteration, where u, v are 
# cells in a column m on the ith iteration. 

# Then dp[(i, u, v)] is largest of the parents (i.e. i-1th iteration) that can get to 
# cell u, v plus grid[u] plus grid[v] (if u != v). 

# The parents are the 9 permuations of (u-1, u, u+1) and (v-1, v, v+1) since from there, we 
# can get to u and v. 

# At the end we take the larest of combos u, v on the mth row for our answer. 

# Time: m*n*n for n columns, m rows. for each ith row, we 
# keep track of entry u, v across n columns. 
# Space: Can optimize to O(N*N). We only need previous and current ith iteration. 

def cherryPickup1(grid):
    dp = {} # (i, u, v) ith row, (u, v) in columns 
    dp[(0, 0, len(grid[0]) - 1)] = grid[0][0] + grid[0][len(grid[0]) - 1]

    for i in range(1, len(grid)):
    # iterate across each pair of u, v in the row; u == v is ok
        for u in range(len(grid[0])):
            for v in range(u, len(grid[0])):
                uvMax = -inf
                for x in [u-1, u, u+1]:
                    cur = -inf
                    for y in [v-1, v, v+1]:
                        if 0 <= x < len(grid[0]) and 0 <= y < len(grid[0]) and (i-1, x, y) in dp:
                            cur = dp[(i-1, x, y)] + grid[i][u]
                            if u != v: cur += grid[i][v]                    
                            uvMax = max(cur, uvMax)
                if uvMax != -inf: dp[(i, u, v)] = uvMax

    res = -inf    
    for u in range(len(grid[0])):
        for v in range(u, len(grid[0])):
            if (len(grid)-1, u, v) in dp: res = max(res, dp[(len(grid)-1, u, v)])
    return res



def cherryPickup(grid):
    dpPrev = {} # (u, v) in columns 
    dpCur = {}  # (u, v) in columns 
    dpPrev[(0, len(grid[0]) - 1)] = grid[0][0] + grid[0][len(grid[0]) - 1]

    for i in range(1, len(grid)):
    # iterate across each pair of u, v in the row; u == v is ok
        for u in range(len(grid[0])):
            for v in range(u, len(grid[0])):
                uvMax = -inf
                for x in [u-1, u, u+1]:
                    cur = -inf
                    for y in [v-1, v, v+1]:
                        if 0 <= x < len(grid[0]) and 0 <= y < len(grid[0]) and (x, y) in dpPrev:
                            cur = dpPrev[(x, y)] + grid[i][u]
                            if u != v: cur += grid[i][v]                    
                            uvMax = max(cur, uvMax)
                if uvMax != -inf: dpCur[(u, v)] = uvMax

        dpPrev, dpCur = dpCur, {}

    res = -inf    
    for u in range(len(grid[0])):
        for v in range(u, len(grid[0])):
            if (u, v) in dpPrev: res = max(res, dpPrev[(u, v)])
    return res




# test cases

grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]

# grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
print(cherryPickup(grid))