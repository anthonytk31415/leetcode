## graphs

from collections import defaultdict, deque
from math import inf

## adjacency list representation
class Graph: 
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)


# print(g.graph)

class BFSNode:
    def __init__(self, name):
        self.name = name
        self.color = 'white'
        self.distance = inf
        self.predecessor = None

# create a nodes dictionary relative to start that traverses breadh first
# from start; information in the nodes dictionary contains shortest distance 
# and predecessor 

def bfs(g, start):
    paths = {}
    for vertex in g.graph:
        paths[vertex] = BFSNode(vertex)
    paths[start].color = 'gray'
    paths[start].distance = 0
    q = deque()
    q.append(start)
    while q:
        u = q.popleft()
        for v in g.graph[u]:
            if paths[v].color == 'white':
                paths[v].color = 'gray'
                paths[v].distance = paths[u].distance + 1
                paths[v].predecessor = u
                q.append(v)
        paths[u].color = 'black'
    return paths

def shortestPath(paths, v):
    print(f'total distance: {paths[v].distance}')
    path = [paths[v].name]
    pred = paths[v].predecessor
    while pred: 
        path = [paths[pred].name] + path
        pred = paths[pred].predecessor
    path = [paths[pred].name] + path
    print(path)

## examples
paths_0 = bfs(g, 0)

# print(paths_0[0].distance)
# print(inf > 3)

# shortestPath(paths_0, 3)


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
# print(g1.graph)


paths1 = bfs(g1, 0)
shortestPath(paths1, 4)


# def dfs(g): 
