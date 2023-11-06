## topological sort

# on DAGs only - directed acyclic graphs; 
# if cycle detected, return False
# else: Return a topological sort of a graph

from collections import defaultdict

class Graph:
    def __init__(self):
        self.g = defaultdict(list)
        self.parent = None
        self.visited = None
        self.processed = None
        self.enter = None
        self.exit = None
        self.time = None
        self.top = None
        self.cycle = False

    def addEdge(self, u, v):
        self.g[u].append(v)

    def dfs(self):
        self.parent, self.visited, self.processed, self.enter, self.exit, self.time, self.top = {}, {}, {}, {}, {}, 0, []  

        def dfs_helper(self, u):
            self.visited[u] = True
            self.time +=1
            self.enter[u] = self.time

            for v in list(self.g[u]): 
                if v not in self.visited: 
                    self.parent[v] = u
                    dfs_helper(self, v)
                else: 
                    self.cycle = True
            self.processed[u] = True
            self.time +=1
            self.exit[u] = self.time
            self.top.append(u)

        for src in list(self.g): 
            if src not in self.processed:
                self.parent[src] = None
                dfs_helper(self, src)

g = Graph()
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(3, 5)
g.addEdge(5, 6)
g.addEdge(6, 7)
g.addEdge(7, 5)

g.dfs()
print(g.top)
print(g.cycle)