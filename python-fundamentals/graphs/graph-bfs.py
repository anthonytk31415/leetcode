# graph search functions


from collections import defaultdict, deque
from math import inf

# create a Breadth First Search and related functions on Graphs

# Time: O(V + E)
# Space: O(V + E)

class Graph: 
    def __init__(self):
        self.g = defaultdict(list)
        self.discovered = {}
        self.processed ={}
        self.parent = {}
        self.distance = {}
        self.directed = True
        self.nedges = 0         # use bfs to calculate nedges
        self.nconnecedComponents = None
        self.color = {}         # use for twocolor
        self.bipartite = None

    def addEdge(self, u, v):
        self.g[u].append(v)

    def initialize_search(self):
        for v in self.g: 
            self.discovered[v], self.processed[v], self.parent[v], self.distance[v] = False, False, None, inf

    #use to count edges
    # def processEdge(self, u, v):
        # self.nedges +=1




    #note to call bfs, you'll need to first call initialize_search first
    def bfs(self, start):
        q = deque()
        q.append(start)
        self.discovered[start] = True
        self.distance[start] = 0
        while q: 
            u = q.popleft()
            self.processed[u] = True
            #process vertex early
            for v in self.g[u]:
                if self.processed[v] == False or self.directed:
                    self.processEdge(u, v)
                if self.discovered[v] == False: 
                    self.distance[v] = self.distance[u] + 1
                    self.discovered[v] = True
                    self.parent[v] = u
                    q.append(v)
            #process vertex late

    # finds the min path and returns an array of that path; min path based on BFS
    def find_path(self, start, end):
        if start == end or not end:
            return [start]
        else:
            return self.find_path(start, self.parent[end]) + [end]

    # returns the number of connected component groups. e.g 1 if all are connected
    def connected_components(self):
        c = 0
        self.initialize_search()
        for v in self.g:
            if self.discovered[v] == False: 
                c +=1
                self.bfs(v)
        self.nconnecedComponents = c

    # this def of processEdge used for bipartite
    def processEdge(self, u, v):
        if self.color[u] == self.color[v]: 
            self.bipartite = False
            print(f'Warning: not bipartite due to {u} and {v}')
        self.color[v] = self.complement(self.color[u])

    # tests for bipartite
    def twocolor(self):
        for v in self.g:
            self.color[v] = 'uncolored'
        self.bipartite = True
        self.initialize_search()
        for v in self.g: 
            if self.discovered[v] == False:
                self.color[v] = 'white'
                self.bfs(v)

    @staticmethod
    def complement(color):
        if color == 'white': 
            return 'black'
        if color == 'black': 
            return 'white'
        return 'uncolored'            

g = Graph()
g.addEdge(0, 1)
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(2, 1)
g.addEdge(2, 3)
g.addEdge(3, 2)


# g1 = Graph()
# g1.addEdge(0,1)
# g1.addEdge(0,2)
# g1.addEdge(0,3)
# g1.addEdge(1,0)
# g1.addEdge(1,2)
# g1.addEdge(1,3)
# g1.addEdge(2,0)
# g1.addEdge(2,1)
# g1.addEdge(2,3)
# g1.addEdge(3,0)
# g1.addEdge(3,1)
# g1.addEdge(3,2)
# g1.addEdge(3,4)
# g1.addEdge(4,3)
# g1.addEdge(4,5)
# g1.addEdge(4,6)
# g1.addEdge(5,4)
# g1.addEdge(5,6)
# g1.addEdge(6,4)
# g1.addEdge(6,5)
# g1.addEdge(6,7)
# g1.addEdge(7,6)
# g1.addEdge(8,9)
# g1.addEdge(9,8)

# g1.initialize_search()
# g1.bfs(0)

g.twocolor()
print(g.bipartite)

# print(g1.parent)
# print(g1.find_path(0,7))
# print(g1.nedges)


# g1.connected_components()
# print(g1.nconnecedComponents)

## connected components
# start a counter c = 0
# loop: for each vertex, if it's not discovered, call bfs and increment c +=1
# return counter c


# def dfsRecursion(g, start):
#     time={'time':0}
#     paths = {}
#     for v in g.g: 
#         paths[v]={'enter': None, 'exit': None, 'parent': None, 'status': 'undiscovered'}
    
#     def helper(g, start, time, paths):
#         paths[start]['status']=time['discovered']
#         paths[start]['enter']=time['time']
#         time['time'] +=1
#         for v in g.g[start]:
#             if paths[v]['status'] == 'undiscovered':
#                 paths['parent'] = start
#                 helper(g, v, time, paths)
#         paths[start]['status']=time['processed']
#         time['time'] +=1 
#         paths[start]['exit']=time['time']
#     helper(g, start, time, paths)
    # return paths
