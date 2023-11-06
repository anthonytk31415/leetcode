
# Time: O(n) you might traverse the nodes twice; once per cycle
# Space: O(n)

## traverse all nodes one at a time via dfs until all are visited
## keep a path for the current dfs; 
## to detect a cycle, your visited node must be in that path
##  --> keep an array to recycle through that node to count cycle length 
## when you're done, add those nodes to an overall visited node
## in a new path, if you hit a visited node

## if you hit a visited node that was 

from math import inf

def longestCycle(edges):
    visited = set()     # you've traversed here and don't want to re-traverse
    cycle = set()       # candidates for a cycle
    def traverse(edges, src, path, visited, cycle):
        cur = src
        while True: 
            if edges[cur] == -1:
                break
            if edges[cur] in path: 
                cycle.add(edges[cur])
                break
            if edges[cur] in visited: 
                break
            else: 
                path.add(edges[cur])
                cur = edges[cur]

        for x in path: 
            visited.add(x)

    for i in range(len(edges)):
        if i not in visited: 
            traverse(edges, i, set([i]), visited, cycle)
    
    if cycle == set(): 
        return -1  
    
    max_cycle = -inf
    for x in cycle: 
        count = 1
        initial = x
        while initial != edges[x]:
            count +=1
            x = edges[x]
        if max_cycle < count: 
            max_cycle = count
    return max_cycle


# x = [3,3,4,2,3]
x = [2,-1,3,1]
print(longestCycle(x))