# bellman ford

# Find the shortest path tree of a graph 
# can handle neg weights
# used on directed graphs neg weights
# can be used on undirected graphs w/ pos eights only

# Time: O(V*E)
# Space: O(V)

# Idea: 
# - input is a list of edges with weights in the format [edges[i]] where edges[i] = [u,v,w]
# - instantiate: dist array = inf for all i
# - dist[src] = 0
# - iterate over v - 1 times: (# this is an "edges" graph algorithm: you need to relax the edges V-1 times)
#   - iterate over all u,v,w edges: 
#       - if dist[u] not inf, relax vertex[u]: dist[v] = dist[u] + w
# - one final loop for negative cycles: iterate over all edges again: 
#   - if dist[u] not inf and relax condition is met: return False
# else, you have no neg cycles, and return the dist




from math import inf 


class Graph:
    def __init__(self, vertices):
        self.g = []
        self.v = vertices

    def addEdge(self, u,v,w):
        self.g.append([u,v,w])

    def bellmanFord(self, src):
        dist = [inf] * self.v
        dist[src] = 0

        for _ in range(self.v - 1):
            for u, v, w in self.g: 
                if dist[u] != inf and dist[v] >  dist[u] + w: 
                    dist[v] = dist[u] + w
        
        for u, v, w in self.g: 
            if dist[u] != inf and dist[v] > dist[u] + w: 
                return False
        
        return dist

# ------------------ rewrite ------------------ #

class Graph1: 
    def __init__(self, vertices):
        self.v = vertices
        self.g = []

    def addEdge(self, u, v, w):
        self.g.append([u,v,w])

    def bellmanFord(self, src):
        dist = [inf] * self.v
        dist[src] = 0
        for _ in range(self.v):
            for u,v,w in self.g:
                if dist[u] != inf and dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
        
        for u,v,w in self.g:
            if dist[u] != inf and dist[v] > dist[u] + w:
                return False

        return dist
 
##------------------------------ rewrite ------------------------------##

class Graph3:
    def __init__(self, vertices):
        self.v = vertices
        self.g = []
    
    def addEdge(self, u,v,w):
        self.g.append([u,v,w])
    
    def bellmanFord(self, src):
        dist = [inf]*self.v
        dist[src] = 0

        for _ in range(self.v - 1):
            for u,v,w in self.g:  
                if dist[u] != inf and dist[v] > dist[u] + w:        # perform the relaxation when the starting vertex has been relaxed
                    dist[v] = dist[u] + w

        # check for negative cycles
        for u,v,w in self.g: 
            if dist[v] != inf and dist[v] > dist[u] + w:
                return False 
        return dist

g = Graph3(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)

print(g.bellmanFord(0))