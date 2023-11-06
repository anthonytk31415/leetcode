from collections import defaultdict, deque
from math import inf


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u,v):
        self.graph[u].append(v)

# Time complexity O(V + E)
# Space Complexity: O(V)
def bfs(g, start):
    visited = {}
    dist = {}
    pred = {}
    for vertex in g.graph:
        visited[vertex] = False
        dist[vertex] = inf
        pred[vertex] = None
    dist[start] = 0
    visited[start] = True
    q = deque()
    q.append(start)
    while q:
        u = q.popleft()
        for v in g.graph[u]:
            if not visited[v]: 
                visited[v] = True
                dist[v] = dist[u] + 1
                pred[v] = u
                q.append(v)
    paths = {}
    for x in visited: 
        paths[x] = {}
        paths[x]['dist'] = dist[x]
        paths[x]['pred'] = pred[x]
    return paths



# min_traversal:
# returns the path from start of the "paths" 
# to the node in the min traversal time 
def min_traversal(paths, node):
    res = deque()
    current = node
    while current:
        res.appendleft(current)
        current = paths[current]['pred']
    res.appendleft(current)
    return res




################################################ 
# example 
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

# x = bfs(g, 0)
# print(x)

##################################################################
## testing and examples: 
g1 = Graph()
g1.addEdge(0,1)
g1.addEdge(0,2)
g1.addEdge(0,3)
g1.addEdge(1,0)
g1.addEdge(1,2)
g1.addEdge(1,3)
g1.addEdge(2,0)
g1.addEdge(2,1)
g1.addEdge(2,3)
g1.addEdge(3,0)
g1.addEdge(3,1)
g1.addEdge(3,2)
g1.addEdge(3,4)
g1.addEdge(4,3)
g1.addEdge(4,5)
g1.addEdge(4,6)
g1.addEdge(5,4)
g1.addEdge(5,6)
g1.addEdge(6,4)
g1.addEdge(6,5)
g1.addEdge(6,7)
g1.addEdge(7,6)

x1 = bfs(g1, 0)
print(x1)
print(min_traversal(x1, 4))