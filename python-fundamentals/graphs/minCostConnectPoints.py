#417

# prims/Kruskalls 
# Time: O(M^2)
# Space: O(M^2)


#manhattan dist
def m_dist(u, v): 
    x1, y1 = u
    x2, y2 = v
    return abs(x2 - x1) + abs(y2 - y1)  

from math import inf

def minDist(m, dist, mst):
    min_v, minIndex = inf, None
    for v in range(m): 
        if not mst[v] and dist[v] < min_v: 
            min_v = dist[v]
            minIndex = v
    return minIndex

def minCostConnectPoints(points):
    m = len(points)

    #set up graph
    graph = [[0 for col in range(m)] for row in range(m)]
    for i in range(m):
        for j in range(m):
            graph[i][j] = m_dist(points[i], points[j])

    mst = [False]*m
    dist = [inf]*m
    src = 0
    dist[src] = 0
    total_dist = 0
    for _ in range(m):
        u = minDist(m, dist, mst)
        total_dist += dist[u]
        mst[u] = True
        for v in range(m):
            if not mst[v] and graph[u][v] >0 and dist[v] > graph[u][v]: 
                dist[v] = graph[u][v]
    # print(dist)
    return total_dist

points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
print(minCostConnectPoints(points))


## first set up the graph