# Time: O(m*n)
# space: O(m*n) to keep track of visited 

# apply DFS; if you hit a visited; you hit a cycle.
# - include a "last" to prevent artificial cycles
# - ru through all nodes if you haven't visited them to test for all paths

def containsCycle(grid): 
    visited = set()

    def dfs(grid, src, visited, last):
        if src in visited: 
            return True
        visited.add(src)
        (i,j) = src
        for (u,v) in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
            if ((u,v) != last and 0 <= u < len(grid) and 0 <= v < len(grid[0]) and 
                grid[i][j] == grid[u][v]):
                if dfs(grid, (u,v), visited, (i,j)): 
                    return True

    #perform dfs on all nodes if not visited; stop if you hit True; 
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            u = (i,j)
            if u not in visited: 
                if dfs(grid, u, visited, None):
                    return True
    return False

# grid = [["a","a","a","a"],
#         ["a","b","b","a"],
#         ["a","b","b","a"],
#         ["a","a","a","a"]]

grid = [["d","b","b"],
        ["c","a","a"],
        ["b","a","c"],
        ["c","c","c"],
        ["d","d","a"]]

# grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
print(containsCycle(grid))