# bfs-practice2.py


from collections import defaultdict, deque
from math import inf

class Graph:
    def __init__(self): 
        self.g = defaultdict(list)
    
    def addEdge(self, u, v):
        self.g[u].append(v)


def bfs(graph, start):
    paths = {}
    for v in graph.g:
        paths[v] = {}
        paths[v]['visited'], paths[v]['dist'], paths[v]['parent']= False, inf, None
    q = deque()
    paths[start]['visited'], paths[start]['dist'] = True, 0
    q.append(start)
    while q: 
        u = q.popleft()
        for v in graph.g[u]:
            if not paths[v]['visited']:
                paths[v]['visited'] = True
                paths[v]['dist'] = paths[u]['dist'] + 1
                paths[v]['parent'] = u
                q.append(v)
    return paths

def shortestPath(paths, end): 
    node = end
    res = deque()
    while node:
        res.appendleft(node)
        node = paths[node]['parent']
    res.appendleft(node)
    return res


        
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

paths = bfs(g, 0)
print(paths)

print(shortestPath(paths, 3))


