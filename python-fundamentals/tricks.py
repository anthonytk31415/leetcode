# a = [[1,2],[3,4],[5,6]]
# b = [[y for y in x] for x in a]
# dist = list(map(lambda i: list(map(lambda j: j,i)), a))     ## this just makes a copy 

# print(dist)
# print(b)

# Floyd Warshall 

# Time: O(V^3)
# Space: O(V^2)

## graph represents a directed path from u to v for graph[u][v]
## if no path exists, then path = inf

from math import inf 

def floydWarshall(graph):
    dist = [[y for y in x] for x in graph]
    print(dist)
    n = len(graph)     
    for k in range(n):
        for i in range(n):
            if i == k: 
                continue
            for j in range(n):
                if j == k:
                    continue 
                else: 
                    print(i,j)
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

graph = [[0, 5, inf, 10],
         [inf, 0, 3, inf],
         [inf, inf, 0,   1],
         [inf, inf, inf, 0]]

print(floydWarshall(graph))