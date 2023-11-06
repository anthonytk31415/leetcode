# bfs and dfs rewrite

from collections import defaultdict, deque

# class Graph:
#     def __init__(self):
#         self.g = defaultdict(list)
#         self.dist = None
#         self.parent = None
#         self.visited = None
#         self.processed = None

#     def addEdge(self, u, v):
#         self.g[u].append(v)
    
#     def bfs(self, src):
#         self.dist, self.parent, self.visited, self.processed = {}, {}, {}, {}
#         self.dist[src] = 0
#         self.parent[src] = None
#         q = deque()
#         q.append(src)
#         while q: 
#             u = q.popleft()
#             self.visited[u] = True
#             for v in self.g[u]:
#                 if v not in self.visited:
#                     q.append(v)
#                     self.parent[v] = u
#                     self.dist[v] = self.dist[u] + 1
#             self.processed[u] = True
    
#     def findPath(self, v):
#         res = []
#         node = v
#         while node: 
#             res = [node] + res
#             node = self.parent[node]
#         res = [node] + res
#         return res

class Graph:
    def __init__(self):
        self.g = defaultdict(list)
        self.time = None
        self.parent = None
        self.enter = None
        self.exit = None
        self.visited = None
        self.processed = None

    def addEdge(self, u, v):
        self.g[u].append(v)

    def dfs(self, src):
        self.visited, self.processed, self.enter, self.exit, self.parent, self.time = {}, {}, {}, {}, {}, 0 
        def dfs_helper(self, u):
            self.visited[u] = True
            self.time +=1
            self.enter[u] = self.time
            for v in self.g[u]:
                if v not in self.visited:
                    self.parent[v] = u
                    dfs_helper(self, v)
            self.processed[u] = True
            self.time +=1
            self.exit[u] = self.time

        self.parent[src] = None
        dfs_helper(self, src)

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.dfs(0)
print(g.parent)


### bipartite
## build cycle detection
## do this for not necessarily connected graphs


### strongly connected components

##