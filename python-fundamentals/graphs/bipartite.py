## test for bipartite graph

#extension of bipartite on a connecteed graph for unconnected graphs:
# - we do the core loop of bipartite on each vertex v if v is not visited; add the vertex one at a time and call the core loop, and do so until all verteces are visited
# - we initiate each core loop with color = 0
# - if at any time we get the color of parent == color of child: return False (but only on verteces that have been visited)

# Time and Space: O(V + E)

from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.g = defaultdict(list)

    def addEdge(self, u,v):
        self.g[u].append(v)

def bipartite(graph):
    parent, visited, color, processed = {}, {}, {}, {}
    q = deque()
    while len(visited) < len(graph):
        if not q:
            for x in range(len(graph)):
                if x not in visited:
                    q.append(x)
                    color[x] = 0
                    visited[x] = True
                    parent[x] = None
                    break 
        while q:
            u = q.popleft()
            print(f'{u} is being visited')
            for v in graph[u]:
                if v not in visited: 
                    parent[v] = u
                    visited[v] = True
                    color[v] = 1 - color[u]
                    q.append(v)
                elif v in visited and color[v] == color[u]:
                    return False
            processed[u] = True
    return True

def bipartite2(graph, start):
    pass


g = Graph()
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(4,1)
g.addEdge(5,6)
g.addEdge(6,5)
print(g.g)
print(bipartite(g.g))