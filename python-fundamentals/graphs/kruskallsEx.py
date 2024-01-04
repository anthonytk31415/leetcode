from heapq import heappush, heappop
from math import inf 

def kruskalls(graph, start):
    queue = [[0, start]]
    vertices = set([x for x in graph])
    dist = {}
    for x in vertices: dist[x] = inf
    dist[start] = 0

    parent = {}
    parent[start] = -1
    visited = set()
    while queue: 
        curDist, u = heappop(queue)
        visited.add(u)
        dist[u] = min(curDist, dist[u])
        for v, vDist in graph[u]:
            if v not in visited and vDist < dist[v]: 
                heappush((vDist, v))



    return parent
