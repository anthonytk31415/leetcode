from collections import deque, defaultdict
from math import inf

class Graph:
    def __init__(self):
        self.g = defaultdict(list)
        self.enter = {}
        self.exit = {}
        self.time = 0
        self.parent = {}
        self.discovered = {}
        self.processed = {}
        self.finished = None
        self.directed = True

    def addEdge(self, u, v):
        self.g[u].append(v)

    def initialize_search(self):
        for v in self.g:
            self.processed[v] = self.discovered[v] = False
            self.parent[v] = None

    # return array of path based on search method
    def find_path(self, start, end):
        if start == end or not end: 
            return [start]
        else: 
            return self.find_path(start, self.parent[end]) + [end]


    # for finding cycles: 
    def process_edge(self, x, y):
        if self.parent[x] != y: 
            print(f'A cycle is found from {y} to {x}')
            print(self.find_path(y, x))
            self.finished=True

    def dfs(self, u):
        if self.finished: 
            return
        self.discovered[u] = True
        self.time +=1
        self.enter[u] = self.time
        #self.process_vertex_early(u)
        for v in self.g[u]:
            if self.discovered[v] == False: 
                self.parent[v] = u
                self.process_edge(u, v)
                self.dfs(v)
            elif self.processed[v] == False or self.directed:
                self.process_edge(u,v)
            if (self.finished):
                return 
        #self.process_vertex_late(u)

        self.time +=1
        self.exit[u] = self.time
        self.processed[u] = True



## finding cycles
## articulation vertices
## topological search
## strongly connected components

## as an exercise, write a standalone program without the "modifying functions" such as initiate_search, process_early, etc.    






g = Graph()
# g.addEdge(0, 1)
# # g.addEdge(1, 0)
# g.addEdge(1, 2)
# # g.addEdge(2, 1)
# g.addEdge(2, 3)
# # g.addEdge(3, 2)
# # g.addEdge(3, 3)

g.addEdge(8, 1)
g.addEdge(1, 8)
g.addEdge(1, 7)
g.addEdge(1, 2)
g.addEdge(7, 1)
g.addEdge(7, 2)
g.addEdge(2, 1)
g.addEdge(2, 7)
g.addEdge(2, 5)
g.addEdge(2, 3)
g.addEdge(3, 2)
g.addEdge(3, 4)
g.addEdge(3, 5)
g.addEdge(5, 2)
g.addEdge(5, 3)
g.addEdge(5, 4)
g.addEdge(5, 6)
g.addEdge(4, 3)
g.addEdge(4, 5)
g.addEdge(6, 5)

print(g.g)

g.initialize_search()
# print(g.discovered)
g.dfs(8)
print(g.enter, g.exit)
print(g.parent)