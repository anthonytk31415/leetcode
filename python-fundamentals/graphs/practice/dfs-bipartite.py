from collections import defaultdict, deque
from math import inf

class Graph: 
    def __init__(self):
        self.g = defaultdict(list)
    
    def addEdge(self, u,v):
        self.g[u].append(v)

def bfs(graph, start):
    paths = {}
    # paths: state, parent, dist
    # state: undiscovered, discovered, processed
    for v in graph.g:
        paths[v] = {}
        paths[v]['state'] = 'undiscovered'
        paths[v]['parent'] = None
        paths[v]['dist'] = inf
    q = deque()
    q.append(start)
    paths[start]['state'] = 'discovered'
    paths[start]['dist'] = 0
    while q: 
        u = q.popleft()
        for v in graph.g[u]: 
            if paths[v]['state'] == 'undiscovered':
                paths[v]['state'] = 'discovered'
                paths[v]['parent'] = u 
                paths[v]['dist'] = paths[u]['dist'] + 1
                q.append(v)
        paths[u]['state'] = 'processed'
    return paths

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print(bfs(g, 0))


def minPath(paths, u):
    res = deque()
    cur = u
    while cur != None:
        res.appendleft(cur)
        cur = paths[cur]['parent']
    return res

print(minPath(bfs(g,0), 3))