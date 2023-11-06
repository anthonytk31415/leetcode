# breadth first search:

from collections import defaultdict, deque

class Graph: 
    def __init__(self, vertices):
        self.g = defaultdict(list) 
        self.v = vertices

    def addEdge(self, u, v):
        self.g[u].append(v)

    def bfs(self, src):
        visited = [False]*self.v
        processed = [False]*self.v
        dist=  [None]*self.v
        parent = [None]*self.v
        q = deque()
        dist[src] = 0
        parent[src] = -1
        q.append(src)

        while q: 
            u = q.popleft()
            visited[u] = True
            for v in self.g[u]:
                if not visited[v]: 
                    parent[v] = u
                    dist[v] = dist[u] + 1
                    q.append(v)
            processed[u] = True
        
        return dist

### bipartite

class Graph1: 
    def __init__(self, vertices):
        self.g = defaultdict(list) 
        self.v = vertices
        self.color = [-1] *vertices

    def addEdge(self, u, v):
        self.g[u].append(v)

    def bfs(self, src):
        visited = [False]*self.v
        processed = [False]*self.v
        dist=  [None]*self.v
        parent = [None]*self.v
        q = deque()
        dist[src] = 0
        parent[src] = -1
        self.color[src] = 0
        q.append(src)
        while q: 
            u = q.popleft()
            visited[u] = True
            for v in self.g[u]:
                if visited[v]: 
                    if self.color[v] == self.color[u]: 
                        return False
                elif not visited[v]: 
                    self.color[v] = 1-self.color[u]
                    parent[v] = u
                    dist[v] = dist[u] + 1
                    q.append(v)
            processed[u] = True
        
        return True



g = Graph1(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
# g.addEdge(2, 0)
g.addEdge(2, 3)
# g.addEdge(3, 3)

print(g.bfs(0))
