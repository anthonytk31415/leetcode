from collections import defaultdict, deque

# bipartite on not necessarily connected graphs
# instantiate: build parent, color, visited, processed checks for each vertex in graph
# iterate over vetices if not processed: add one vertex into queue and start the while loop to color the connected vertices
# do BFS: 
# - assign first color, then for each child of parent, assign color = complement of parent if not visited, then add to queue to iterate of child's children
# - if the color of parent == color of child --> FALSE
# this runs in O(V+E) time; space  in O(V)

class Graph:
    def __init__(self):
        self.g = defaultdict(list)
        self.dist = None
        self.parent = None
        self.visited = None
        self.processed = None
        self.color = None
    def addEdge(self, u, v):
        self.g[u].append(v)
    
    def bipartite(self):
        self.dist, self.parent, self.visited, self.processed, self.color = {}, {}, {}, {}, {}
        q = deque()

        for w in self.g:
            if w not in self.processed:  
                self.dist[w] = 0
                self.parent[w] = None
                self.color[w] = 1
                q.append(w)
                while q: 
                    u = q.popleft()
                    self.visited[u] = True
                    for v in self.g[u]:
                        if v not in self.visited:
                            q.append(v)
                            self.color[v] = 1 - self.color[u]
                            self.parent[v] = u
                            self.dist[v] = self.dist[u] + 1
                        if self.color[v] == self.color[u]:
                            return False
                    self.processed[u] = True
        return True

g = Graph()
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(4,1)
g.addEdge(5,6)
g.addEdge(6,5)
g.addEdge(3,1)
g.addEdge(1,3)
print(g.g)
print(g.bipartite())
print(g.color)