
# - for each city, find the number of cities reachable in a distance 
#     - to do this, do bfs on cities until you can traverse no longer
#     - once you reach a city, append to res and only go to visited cities 
#     - bfs candidates are those that have a distanceThreshold 
# - then collect the city with min traveled cities; if tie, take the one with max index 


# revision: it's shortest path tree across all vertices for source; then take all vertices <= dist threshold
# use Floyd Warshall to find shortest path across all pairs to get the matrix
# then across each i,j, return 1 if the dist[i][j] <= threshold, 0 otherwise, then return the sum for each row 
# then find the min row; if tiebreaker for the min row; take the latest row 

# Time: O(v^3)
# space: O(v^2) for one matrix

from math import inf
def findTheCity(n, edges, distanceThreshold):

    dist = [[inf for _ in range(n)] for _ in range(n)]
    for d in range(n):
        dist[d][d] = 0
    
    for i in range(len(edges)):
        u,v,w = edges[i]
        dist[u][v] = w
        dist[v][u] = w
    
    # floyd warshall: iterate over vertices; if dist < oldl dist: replace

    for k in range(n):
        for i in range(n):
            if i == k: continue
            for j in range(n):
                if j == k: continue
                dist[i][j] = min(dist[i][j],  dist[i][k] + dist[k][j])
    
    res = [[1 for x in row if x <= distanceThreshold] for row in dist]
    res = [sum(row) for row in res]
    minCities = inf
    minCity = None
    for i in range(len(res)):
        if res[i] <= minCities: 
            minCities = res[i]
            minCity = i
    return minCity

# n = 4
# edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
# distanceThreshold = 4



n = 5
edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
distanceThreshold = 2

print(findTheCity(n, edges, distanceThreshold))