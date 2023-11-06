##############################################################################################################
# Graph

## Kruskals - given a weighted graph, use union find to find the min spanning tree by recursively choosing v-1 min edges with no cycles 
## Prim - like dijkstra, choose min dist from src to find min spanning tree by traversing v nodes 
## Dijkstra - find shortest path tree on a undirected graph with weights by traversing and relaxing edges and choosing the path to a vertex with min dist v times
# Bellman - find shortest path tree with negative weights on a connected, no cycles graph; do edge relaxation starting on source v-1 times; if done one more time and yields a shorter dist; you have a cycle and you can't have
# 
##############################################################################################################

#######################################################
# Djikstra's 
# Find the shortest path from a source to any vertex on an undirected graph with weights

from math import inf

class Graph: 
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

    def dijkstra(self, src): 
        spt = [False] * self.v
        dist = [inf] * self.v
        dist[src] = 0
        parent = [-1] * self.v
        for _ in range(self.v):
            u = self.minDist(dist, spt)
            spt[u] = True 
            for v in range(self.v):
                if not spt[v] and self.g[u][v] > 0 and dist[v] > dist[u] + self.g[u][v]:
                    dist[v] = dist[u] + self.g[u][v]
                    parent[v] = u
        return parent, dist

g = Graph(9)
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
print('Djikstras:')
print(g.dijkstra(0))



#######################################################
# prim
class Graph2:
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

    def prim(self, src):
        mst = [False] * self.v
        dist = [inf] * self.v
        parent = [None] * self.v
        dist[src] = 0
        parent[src] = -1
        for _ in range(self.v):
            u = self.minDist(dist, mst)
            mst[u] = True
            for v in range(self.v):
                if not mst[v] and self.g[u][v] > 0 and dist[v] > self.g[u][v]:
                    dist[v] = self.g[u][v]
                    parent[v] = u
        return parent


# g = Graph2(5)
# g.g = [[0, 2, 0, 6, 0],
#             [2, 0, 3, 8, 5],
#             [0, 3, 0, 0, 7],
#             [6, 8, 0, 0, 9],
#             [0, 5, 7, 9, 0]]

# z = g.prim(0)
# print(z)

# >> ([-1, 0, 1, 0, 1], [0, 2, 3, 6, 5])

#######################################################
# kruskal's 

class Graph3:
    def __init__(self, vertices):
        self.g = []                   # contains array of edges and weights; g[i] = [u,v,w] for u -> v with weight = w
        self.v = vertices

    def addEdge(self, u,v,w):
        self.g.append([u,v,w])

    def find(self, parent, i):
        if parent[i] != i:
            return self.find(parent, parent[i])
        else: 
            return i
    
    def union(self, rank, parent, p_i, p_j):
        if rank[p_i] > rank[p_j]:
            parent[p_j] = p_i

        elif rank[p_i] < rank[p_j]:
            parent[p_i] = p_j

        else: 
            parent[p_j] = p_i
            rank[p_i] +=1

    def kruskal(self):
        parent, rank, res = [], [], []
        self.g.sort(key = lambda x: x[2])     # sort by smallest weights
        for z in range(self.v):
            parent.append(z)            # each i has its parent = i initially
            rank.append(0)
        e, i = 0, 0
        while e < self.v - 1: 
            u,v,w = self.g[i]
            i +=1
            p_u = self.find(parent, u)
            p_v = self.find(parent, v)
            if p_u != p_v: 
                res.append([u,v,w])
                self.union(rank, parent, p_u, p_v)
                e += 1                
        return res 


# g = Graph3(4)
# g.addEdge(0, 1, 10)
# g.addEdge(0, 2, 6)
# g.addEdge(0, 3, 5)
# g.addEdge(1, 3, 15)
# g.addEdge(2, 3, 4)
# print(g.g)
# # Function call
# z = g.kruskal()
# print(z)

#######################################################
# bellman ford 

class Graph4:
    def __init__(self, vertices):
        self.v = vertices
        self.g = []
    
    def addEdge(self, u,v,w):
        self.g.append([u,v,w])

    def bellmanFord(self, src):
        dist = [inf]*self.v
        dist[src] = 0

        for _ in range(self.v - 1):
            for x in self.g: 
                (u,v,w) = x
                if dist[u] != inf and dist[v] > dist[u] + w: 
                    dist[v] = dist[u] + w
        
        for x in self.g: 
            (u,v,w) = x
            if dist[u] != inf and dist[v] > dist[u] + w: 
                return False        # cycle detected

        return dist


g = Graph4(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)

print(g.bellmanFord(0))



# Graph Traversal
#
#
#


##############################################################################################################
# Sorts
# quicksort + quickselect
# mergesort
# counting sort + radix sort


def quicksort(a, p, r):
    # print(a)
    if p < r:
        q = partition(a,p,r)
        quicksort(a,p,q-1)
        quicksort(a,q+1,r)

def partition(a,p,r):
    pivot = a[r]
    i = p-1
    for j in range(p, r):
        if a[j] < pivot: 
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i + 1

a = [3,0,6,5,1,2,7,4]

# quicksort(a,0,7)
# print(a)


def quickselect(a,p,r,k):
    if p <= p + k - 1 <= r:
        q = partition(a,p,r)
        if q == p + k - 1: 
            return a[q]
        elif q > p + k - 1:
            return quickselect(a,p,q-1,k)  
        else: 
            return quickselect(a,q+1,r, q - (p + k - 1))

def mergesort(a,p,r):
    if p >= r: 
        return 
    q = (p + r) // 2
    mergesort(a,p,q)
    mergesort(a,q+1,r)
    merge(a,p,q,r)

def merge(a,p,q,r):
    left = a[p:q+1]
    right = a[q+1:r+1]
    i = 0
    j = 0
    k = p
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a[k] = left[i]
            i +=1
            k +=1
        else: 
            a[k] = right[j]
            j +=1
            k +=1
    while i < len(left): 
        a[k] = left[i]
        i +=1
        k +=1
    while j < len(right):
        a[k] = right[j]
        j +=1
        k +=1

# mergesort(a,0,7)
# print(a)

# print(quickselect(a,0,7,5))



# counting sort

# def countingSort(a):
#     b = [0 for x in a]
#     c = [0] * max(a)


