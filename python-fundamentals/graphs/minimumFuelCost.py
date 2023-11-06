from collections import defaultdict

# do dfs from 0 to get the following: 
# - get total nodes in that node's subtree (including itself) which is 1 + SUM of child nodes (for each child)
# - for each child, COST += child nodes / seats (rounded up)
# 
from math import ceil 

def minimumFuelCost(roads, seats):
    graph = defaultdict(list)
    visited = set()
    for u,v in roads: 
        graph[u].append(v)
        graph[v].append(u)
    
    cost = [0]

    def dfs(u, graph, cost, visited):
        nodes = 1
        visited.add(u)
        for v in graph[u]:
            if v not in visited: 
                v_nodes = dfs(v, graph, cost, visited)
                cost[0] += ceil(v_nodes/seats)
                nodes += v_nodes
        return nodes

    dfs(0, graph, cost, visited)
    return cost[0]

# roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]]
# seats = 2
# 7

roads = [[0,1],[0,2],[0,3]]
seats = 5

print(minimumFuelCost(roads, seats))

