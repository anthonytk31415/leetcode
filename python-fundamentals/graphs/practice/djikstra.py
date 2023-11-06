# practice djikstra
# for a weighted graph with weights as matrix entries, find the shortest weighted path
# where weights >= 0 
# time: O(V)


# Time: O(V+E)
# Space: O(V+E)

from math import inf

# matrix
class Graph: 
    def __init__(self, vertices):
        self.v = vertices
        self.g = [[0 for col in range(vertices)]for row in range(vertices)]

    def minDistance(self, dist, spt):
        min, minIndex = inf, None
        for v in range((self.v)):
            if spt[v] == False and dist[v] < min:
                min, minIndex = dist[v], v
        return minIndex

    def djikstra(self, src):
        dist, spt = [inf]*self.v, [False]*self.v
        dist[src] = 0
        for _ in range((self.v)):
            u = self.minDistance(dist, spt)
            spt[u] = True 
            for v in range((self.v)):
                if spt[v] == False and self.g[u][v] > 0 and dist[v] > dist[u] + self.g[u][v]:
                     dist[v] = dist[u] + self.g[u][v]

        return dist
            
g = Graph(9)
g.g = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]

print(g.djikstra(0))

# >> [0, 4, 12, 19, 21, 11, 9, 8, 14]