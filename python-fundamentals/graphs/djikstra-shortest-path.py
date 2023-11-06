# djikstra's 
# used for shortest weighted path 

# - returns the shortest weighted path graph so that from a given point, you can reach any other point in the shortest path possible
# - will traverse V-1 min edges 
# - can be directed or undirected
# - no negative weights
# - this algo below uses a matrix representation of graph + weights
# - must be connected; if not connected, no shortest path to that unconnected vertex/branch

# Idea: 
# - you'll choose a starting vertex
# - instantiate: create dist array with dist[i]=[inf] for all i vertices; spt[i]=false  for all i; set dist[src] = 0
# - The Loop: iterate over v vertices
#   - choose u = min distance vertex that's not in spt
#   - then for each v child of u that's not in spt, relax the distance:
#       - relax: if dist[v] > dist[u] + graph[u][v] --> dist[v] = dist[u] + graph[u][v]
# - return dist

# Analysis: 
# Time: O(V^2) for each vertex and relaxing its neighbors; can be reduced to O(ElogV) using minheap
# Space: O(V)

# similar to Prim's Algorithm, but you're calculating cumulative distance not just the edge; this mechanism gives you min path rather than total min weights to get to all paths

# To do: 
# build using a graph
# build using minheap and priority queue

from math import inf
from collections import defaultdict

class Graph: 
    def __init__(self, vertices):
        self.v = vertices
        self.g = [[0 for col in range(vertices)] for row in range(vertices)]

    def minDistance(self, dist, spt):
        min, minIndex = inf, None
        for v in range(self.v):
            if not spt[v] and dist[v] < min: 
                min, minIndex = dist[v], v
        return minIndex


    def djikstra(self, src):
        dist, spt = [inf]*self.v, [False]*self.v
        parent = [-1] *self.v
        dist[src] = 0

        for _ in range(self.v):
            u = self.minDistance(dist, spt)
            spt[u] = True
            for v in range(self.v):
                if spt[v] == False and self.g[u][v] > 0 and dist[v] > dist[u] + self.g[u][v]:
                    dist[v] = dist[u] + self.g[u][v]
                    parent[v] = u

        print(dist)
        print(parent)
        return parent

## -------------------------- Rewrites below -------------------------- ##

# class Graph:
#     def __init__(self, vertices):
#         self.v = vertices
#         self.g = [[0 for column in range(self.v)] for row in range(self.v)]
    
#     def minDistance(self, dist, sptSet):
#         min, minIndex = inf, None
#         for v in range(self.v):
#             if dist[v] < min and sptSet[v] == False:
#                 min , minIndex = dist[v], v
#         # print(minIndex)
#         return minIndex

#     def djikstra(self, src):
#         dist = [inf]*self.v                         # distance to be updated as vertices are relaxed
#         dist[src] = 0                               # initialize so it gets picked up in the for loop
#         sptSet = [False]*self.v                     # set of visited vertices
#         for cout in range(self.v):                  # iterate over all vertices
#             print(f'dist = {dist}')
#             u = self.minDistance(dist, sptSet)      # pick the u w/ min distance not in sptSet (i.e. has not been) 
#             print(f'u min dist = {u}')
#             sptSet[u] = True
#             # print(dist[u])
#             for v in range(self.v):                 # relax neighbor vertices 
#                 print(f'u = {u}, v = {v}')
#                 if (self.g[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.g[u][v]): 
#                     print(f'updated vertex: {v}')
#                     dist[v] = dist[u] + self.g[u][v]
#         return dist 



# label 
# youll need some table with edges and the cost 
# you need a start vertex
# label all of the verteces with the cost: 
# - start from the "start" and its children 
# - for the rest, label the cost = inf
# iterative step: 
# choose connected smallest vertex, update the cost, then relax 
# its 
# over the vertex connected iterate of






# spt = shortest path tree

######## rewrite

## Graph matrix representation
# class Graph:
#     def __init__(self, vertices):
#         self.v = vertices
#         self.g = [[0 for column in range(self.v)] for row in range(self.v)]

#     def minDistance(self, dist, spt):
#         min, minIndex = inf, None
#         for v in range(self.v):
#             if not spt[v] and dist[v] < min:
#                 min, minIndex = dist[v], v
#         return minIndex

#     def djikstra(self, src):
#         dist, spt = [inf] * self.v, [0]* self.v
#         dist[src] = 0
    
#         for _ in range(self.v):
#             u = self.minDistance(dist, spt)
#             spt[u] = True

#             for v in range(self.v):
#                 if spt[v] == False and self.g[u][v] > 0 and dist[v] > dist[u] + self.g[u][v]:
#                     dist[v] = dist[u] + self.g[u][v]
#         return dist

# given a set of V vertices and an undirected graph of edges and weights, 
# we can find a minimum path from a source to any of the nodes
# 


# class Graph: 
#     def __init__(self, vertices):
#         self.v = vertices
#         self.g = [[0 for col in range(vertices)] for row in range(vertices)]
    
#     def minDistance(self, dist, spt):
#         min, minIndex = inf, None
#         for v in range(self.v):
#             if not spt[v] and dist[v] < min: 
#                 min, minIndex = dist[v], v
#         return minIndex

#     def djikstra(self, src):
#         dist , spt = [inf] * self.v, [False]*self.v
#         dist[src] = 0
#         for _ in range(self.v):
#             u = self.minDistance(dist, spt)
#             spt[u] = True
#             for v in range(self.v):
#                 if spt[v] == False and self.g[u][v] > 0 and dist[v] > dist[u] + self.g[u][v]:
#                     dist[v] = dist[u] + self.g[u][v]
#         return dist 





##---- another rewrite ---- -##

# class Graph: 
#     def __init__(self, vertices) -> None:
#         self.v = vertices
#         self.g = [[0 for col in range(vertices)] for row in range(vertices)]
    
#     def minDist(self, dist, spt):
#         min, minIndex = inf, None
#         for v in range(self.v):
#             if not spt[v] and dist[v] < min: 
#                 min = dist[v]
#                 minIndex = v
#         return minIndex

#     def djikstra(self, src):
#         dist = [inf] * self.v
#         spt = [False] * self.v
#         dist[src] = 0
#         for _ in range(self.v):
#             u = self.minDist(dist, spt)
#             spt[u] = True
#             for v in range(self.v):
#                 if not spt[v] and self.g[u][v] > 0 and dist[u] + self.g[u][v] < dist[v]:
#                     dist[v] = dist[u] + self.g[u][v]
#         return dist


#--------- another rewrite for fun ------------#

class Graph1: 
    def __init__(self, vertices):
        self.v = vertices
        self.g = [[0 for col in range(vertices)] for row in range(vertices)]
    
    def minDist(self, dist, spt):
        min, minIndex = inf, None
        for v in range(self.v):
            if not spt[v] and dist[v] < min:
                min = dist[v]
                minIndex = v
        return minIndex

    def djikstra(self, src):
        dist = [inf] * self.v
        spt = [False] * self.v
        dist[src] = 0
        for _ in range(self.v):
            u = self.minDist(dist, spt)
            spt[u] = True
            for v in range(self.v):
                if not spt[v] and self.g[u][v] > 0 and dist[v] > dist[u] + self.g[u][v]:
                    dist[v] = dist[u] + self.g[u][v]
        return dist

#--------- another rewrite w/ minheap ------------#


class Graph3:
    def __init__(self, vertices):
        self.v = vertices
        self.g = [[0 for cols in range(vertices)] for row in range(vertices)]

    def minDist(self, dist, spt):
        min, minIndex = inf, None
        for v in range(self.v): 
            if not spt[v] and dist[v] < min: 
                min = dist[v]
                minIndex = v
        return minIndex

    def djikstra(self, src):
        dist = [inf]*self.v
        spt = [False]*self.v
        dist[src] = 0
        for _ in range(self.v):
            u = self.minDist(dist, spt)
            spt[u] = True
            for v in range(self.v):
                if not spt[v] and self.g[u][v] > 0 and dist[v] > dist[u] + self.g[u][v]:
                    dist[v] = dist[u] + self.g[u][v]
        return dist




class Graph4: 
    def __init__(self, vertices):
        self.g = [[0 for col in range(vertices)] for row in range(vertices)]
        self.v = vertices

    def minDist(self, dist, spt):
        min, minIndex = inf, None
        for v in range(self.v):
            if not spt[v] and dist[v] < min: 
                min = dist[v]
                minIndex = v
        return minIndex

    def djikstra(self, src):
        dist = [inf] * self.v
        spt = [False] * self.v
        dist[src] = 0
        parent = [-1]*self.v
        for _ in range(self.v):
            u = self.minDist(dist, spt)
            spt[u] = True
            for v in range(self.v): 
                if not spt[v] and self.g[u][v] > 0 and dist[v] > dist[u] + self.g[u][v]:
                    dist[v] = dist[u] + self.g[u][v]
                    parent[v] = u
        return parent


g = Graph4(9)
#       0, 1, 2, 3, 4, 5, 6, 7, 8
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

