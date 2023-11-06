# https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/

from collections import defaultdict
from math import inf
# graph[u] = (v, w)



# time restrictions!!!???

def countRestrictedPaths(n, edges):

    def minDist(dist, spt):
        min, minIndex = inf, None
        for v in range(len(dist)):
            if not spt[v] and min > dist[v]:
                min = dist[v]
                minIndex = v
        return minIndex

    # (1) build shortest path tree from last node n using dijkstra 
    graph = defaultdict(list)
    for e in edges:
        (u_star,v_star,w) = e
        u = u_star - 1 
        v = v_star - 1
        graph[u].append((v,w))
        graph[v].append((u,w))
    vertices = n                    # note we reindexed stuff so that index starts at 0. so what was 1 is now 0.
    dist = [inf]*vertices #
    spt = [False]*vertices
    src = n-1                       #"start" at n-1
    dist[src] = 0

    for _ in range(vertices):
        u = minDist(dist, spt)
        spt[u] = True
        for z in graph[u]:
            (v,w) = z
            if not spt[v] and dist[v] > dist[u] + w:
                dist[v] = w + dist[u]

    # build the tree of dist restricted node
    start = 0
    memo = {}

    def dfs(u, graph, memo):
        if u in memo: 
            return memo[u]
        else: 
            children = [z[0] for z in graph[u] if dist[u] > dist[z[0]]]
            if not children: 
                memo[u] = 1
            else: 
                res = 0
                for v in children: 
                    res += dfs(v, graph, memo)
                memo[u]=res
            return memo[u]

    return dfs(start, graph, memo) % (10**9 + 7)

n = 6
edges = [[2,1,3574],[4,3,1378],[1,5,38739],[6,1,95222],[5,4,78194],[4,6,41976],[1,4,58963],[4,2,51285],[2,3,41063],[2,6,52240],[5,6,8253],[3,6,8414],[5,3,41596],[1,3,78833]]

print(countRestrictedPaths(n, edges))