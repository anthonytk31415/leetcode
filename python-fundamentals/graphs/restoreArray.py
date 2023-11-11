# https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/?envType=daily-question&envId=2023-11-10

from collections import defaultdict, deque

# In this implementation, I use a queue to queue the next one to process. 
# Prevously I wrote a DFS function as the while loop essentially, but python isn't too happy with it. 
# Time: O(n) to run through each pair 
# Space: O(n) to store the graph as an adjacency list

def restoreArray(adjacentPairs): 

    # build the graph
    graph = defaultdict(list)
    singles = set([])
    for u, v in adjacentPairs: 
        graph[u].append(v)
        graph[v].append(u)
    
        for i in [u, v]:
            if i not in singles: singles.add(i)
            else: singles.remove(i)
    singles = list(singles)

    # this should only have one path: 
    res = []
    start = singles[0]
    queue = deque([start])
    visited = set([])
    while queue: 
        u = queue.popleft()
        visited.add(u)
        res.append(u)
        for v in graph[u]:
            if v not in visited: 
                queue.append(v)

    return res 


    # pick an arbitrary path; dfs and count the path. keep track of your path
    # then dfs the other way . then combine the paths 

# adjacentPairs = [[2,1],[3,4],[3,2]]
# adjacentPairs = [[4,-2],[1,4],[-3,1]]


print(len(adjacentPairs))
print(restoreArray(adjacentPairs))