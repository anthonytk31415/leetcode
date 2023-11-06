# prims
from math import inf

from heapq import heappush, heappop 

# Premise: 
# given a connected, undirected graph, find the min spanning tree (MST)
# - returns a parent graph of each N nodes
# - arbitrarily choose a starting nod


# Properties: 
# - cannot use on nonconnected graphs beause you return a tree a singlel tree; algorithm relies on finding the min child of a chosen vertex due to relaxation
# - Greedy approach
# - Time: O(V^2), but can be improved if we use a minheap
# - Space: O(V)

# Idea: 
# - give a staritng point, 
# - Instantiate a parent and dist (key) array for each i in vertices, with position i = vertex
#   - parent = None; key = inf for all i; then key[start] = 0
# - the loop: iterate across all v vertices
#   - choose the min key[i],i from the Key that's not in the chosen set (mst) (note that min distances will be the ones relaxed) at each iteration from the most recently chosen vertex
#   - for each edge from the minKey, relax it's neighbor's edges
#   - relax: if there's an edge from vertex to child vertex, and edge cost < key (current cost), update teh current cost *(key) = edge cost
# return the parent array, which has for each index its parent. This forms the MST!
# return the sum of distant to get the smallest distance required to traverse
# Note: traversing 


# myHeap = [3]

# heappush(myHeap, 30)
# heappush(myHeap, 15)
# heappush(myHeap, 35)
# heappush(myHeap, 45)
# heappush(myHeap, 7)
# print(myHeap)


# class Graph:
#     def __init__(self, vertices):
#         self.v = vertices
#         self.g = [[0 for col in range(vertices)] for row in range(vertices)]


#     # iterate over options to return the min key Index
#     def minKey(self, key, mstSet):
#         min = inf
#         for v in range(self.v):
#             if key[v] < min and mstSet[v] == False:
#                 min = key[v]
#                 minIndex = v
#         return minIndex

#     def primMST(self):
#         key = [inf] * self.v
#         mstSet = [False] * self.v
#         parent = [None] * self.v
#         key[0] = 0                              # instantiate so we choose this first in loop
#         parent[0] = -1                          # first node's parent is effectively None

#         for _ in range(self.v):
#             u = self.minKey( key, mstSet)  # select the min at each iteration
#             mstSet[u] = True                            
#             for v in range(self.v):
#                 if self.g[u][v] > 0 and mstSet[v] == False and key[v] > self.g[u][v]:
#                     key[v] = self.g[u][v]
#                     parent[v] = u
#         return parent




## matrix representation
class Graph: 
    def __init__(self, vertices):
        self.v = vertices
        self.g = [[0 for col in range(vertices)] for row in range(vertices)]

    def minKey (self, key, mst):
        min, minIndex = inf, None
        for v in range(self.v):
            if mst[v] == False and key[v] < min:
                min = key[v]
                minIndex = v
        return minIndex

    def primMST(self, src):
        key = [inf] * self.v
        mst = [False] * self.v
        parent= [None] * self.v
        parent[src] = -1
        key[src] = 0
        for _ in range(self.v):
            u = self.minKey(key, mst)
            mst[u] = True
            for v in range(self.v):
                if mst[v] == False and 0 < self.g[u][v] < key[v]:
                    key[v] = self.g[u][v]
                    parent[v] = u 
        return parent


class Graph1: 
    def __init__(self, vertices):
        self.v = vertices
        self.g = [[0 for col in range(vertices)] for row in range(vertices)]

    def minDist(self, dist, mst):
        min, minIndex = inf, None
        for v in range(self.v):
            if not mst[v] and dist[v] < min:
                min = dist[v]
                minIndex = v
        return minIndex

    def primMST(self, src):
        parent = [None]* self.v
        dist = [inf] * self.v
        mst = [False] * self.v
        dist[src] = 0
        parent[src] = -1
        for _ in range(self.v):
            u = self.minDist(dist, mst)
            mst[u] = True
            for v in range(self.v):
                if not mst[v] and self.g[u][v] >0 and dist[v] > self.g[u][v]:
                    dist[v] = self.g[u][v]
                    parent[v] = u 
        return parent

class Graph: 

    def __init__(self, vertices) -> None:
        self.v = vertices
        self.g = [[0 for col in range(vertices) for row in range(vertices)]]

    def minDist(self, dist, mst):
        min, minIndex = inf, None
        for v in range(self.v):
            if not mst[v] and dist[v] < min:
                min = dist[v]
                minIndex = v
        return minIndex
    
    def primMST(self, src):
        dist = [inf]*self.v
        parent = [None] * self.v
        mst = [False] * self.v
        parent[src] = -1
        dist[src] = 0
        for _ in range(self.v):
            u = self.minDist(dist, mst)
            mst[u] = True
            for v in range(self.v):
                if not mst[v] and self.g[u][v] >0 and dist[v] > self.g[u][v]:
                    parent[v] = u
                    dist[v] = self.g[u][v]
        return parent

## --------------------------------------------- Rewrite --------------------------------------------- ##

class Graph3: 
    def __init__(self, vertices):
        self.v = vertices
        self.g = [[0 for col in range(vertices)] for row in range(vertices)]
    
    def minDist(self, dist, mst):
        min, minIndex = inf, None
        for v in range(self.v):
            if not mst[v] and dist[v] < min: 
                min, minIndex = dist[v], v
        return minIndex
    
    def primMST(self, src):
        dist = [inf] * self.v
        mst = [False] * self.v
        parent = [None] * self.v
        dist[src] = 0
        parent[src] = -1
        for _ in range(self.v):
            u = self.minDist(dist, mst)
            mst[u] = True
            for v in range(self.v):
                if not mst[v] and self.g[u][v] > 0 and dist[v] > dist[u] + self.g[u][v]:
                    dist[v] = dist[u] + self.g[u][v]
                    parent[v] = u
        return parent 

g = Graph3(5)
g.g = [[0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]

z = g.primMST(0)
print(z)