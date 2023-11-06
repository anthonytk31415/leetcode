# Most Stones Removed with Same Row or Column

#649

def find(parent, i):
    if parent[i] != i: 
        return find(parent, parent[i])
    else: 
        return i

def union(parent, i, j):
    parent[i] = j

# Union Find method
# this takes n^2 applying union find; but it can probably be done quicker
def removeStones(stones):
    
    parent = {}
    for (a,b) in stones: 
        parent[(a,b)]=(a,b)
    for (a,b) in stones: 
        for (c,d) in stones: 
            if (a,b) != (c,d) and (a == c or b == d):
                p_1 = find(parent, (a,b))
                p_2 = find(parent, (c,d))
                if p_1 != p_2: 
                    union(parent, p_1, p_2)
    for x in parent:  
        parent[x] = find(parent, x)

    numSubsets = len(set(parent.values()))

    # return len(stones) - num_subsets
    return len(stones) - numSubsets

# DFS Method
# using DFS could be quicker as we only need to evaluate one node once

def removeStones1(stones):
    visited = {}
    processed = {}
    stones = [(x,y) for [x,y] in stones]
    def dfs_helper(visited, processed, x):
        visited[x] = True
        for z in stones:
            if x != z and z not in visited and (z[0] == x[0] or z[1]==x[1]): 
                dfs_helper(visited, processed, z)
        processed[x] = True

    counter = 0
    for y in stones: 
        if y not in processed: 
            counter +=1
            dfs_helper(visited, processed, y)

    return len(stones) - counter





        
# stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
stones = [[0,1],[1,2],[1,3],[3,3],[2,3],[0,2]]
print(removeStones1(stones))