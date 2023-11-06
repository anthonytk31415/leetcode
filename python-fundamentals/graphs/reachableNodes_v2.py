# build an adjacency list 
# start at 0
# do dfs
# create a visited set
# create a restricted set to check restricted at O(1) cost
# rerturn the length of the visited set

# Time: O(n)
# Space: O(n)

from collections import defaultdict

def reachableNodes(n, edges, restricted):
    graph = defaultdict(list)
    for u,v in edges: 
        graph[u].append(v)
        graph[v].append(u)
    visited = set()
    restricted = set(restricted)

    def dfs(u, graph, visited, restricted):
        visited.add(u)
        for v in graph[u]:
            if v not in visited and v not in restricted: 
                dfs(v, graph, visited, restricted)
    
    dfs(0, graph, visited, restricted)
    return len(visited)