from collections import defaultdict, deque
from math import inf

class Graph: 
    def __init__(self):
        self.g = defaultdict(list)
    
    def addEdge(self, u, v):
        self.g[u].append(v)
    
def dfsRecursion(g, start):
    paths = {}
    time = {'time': 0}
    # statuses: undiscovered > discovered > processed
    for v in g.g: 
        paths[v] = {'entry': None, 'exit': None, 'parent': None, 'status': 'undiscovered'}
    
    def helper(g, start, time, paths): 
        paths[start]['status'] = 'discovered'
        paths[start]['entry'] = time['time']
        time['time'] +=1
        for v in g.g[start]:
            if paths[v]['status'] == 'undiscovered':
                paths[v]['parent'] = start
                helper(g,v,time,paths)
        paths[start]['status'] = 'processed'
        paths[start]['exit'] = time['time']
        time['time'] +=1

    helper(g, start, time, paths)
    return paths


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


# paths = dfsRecursion(g1, 0)

# print(paths)



def dfs2(g, start):
    time = {'time':0}
    paths = {}
    for v in g.g:       # status: 'undiscovered', 'discovered', 'processed'
        paths[v] = {}
        paths[v]['start'], paths[v]['stop'], paths[v]['parent'], paths[v]['status'] = None, None, None, 'undiscovered'
    def helper(g, start, time, paths):
        paths[start]['start'] = time['time']
        time['time'] +=1
        paths[start]['status'] = 'discovered'
        for v in g.g[start]:
            if paths[v]['status'] == 'undiscovered':
                paths[v]['parent'] = start
                helper(g,v,time,paths)
        paths[start]['stop'] = time['time']
        paths[start]['status'] = 'processed'
        time['time'] +=1
    helper(g, start, time, paths)
    return paths


# paths = dfs2(g1, 0)
# print(paths)


def bfs(g,start):
    paths = {}
    q = deque()
    for v in g.g:
        paths[v]= {'parent': None, 'status': 'undiscovered', 'distance': inf }
    q.append(start)
    paths[start]['status'] , paths[start]['distance'] = 'discovered', 0
    while q: 
        u = q.popleft()
        for v in g.g[u]:
            if paths[v]['status'] == 'undiscovered':
                paths[v]['status'] = 'discovered'
                paths[v]['parent'] = u
                paths[v]['distance'] = paths[u]['distance'] +1
                q.append(v)
        paths[u]['status'] = 'processed'
    return paths

pathBFS = bfs(g1, 0)
print(pathBFS)

# def connectedComponents(g):
#     c = 0
#     for 
