# strongly connected components
# represent using adjacency lists
from collections import defaultdict

# return an array of the sets of strongly connected components

# run dfs and get the finish times
# then find the transponse of the graph
# run dfs but do it on vertices by decreasing finish times
# when vertices are 

class Graph:
    def __init__(self) -> None:
        self.g = defaultdict(list)
        self.time = None
        self.g_transpose = defaultdict(list)
        self.processed = None
        self.visited = None
        self.enter = None
        self.exit = None
        self.tree = None                        # use this to append connected nodes in iterative dfs
    
    def addEdge(self, u, v):
        self.g[u].append(v)

    def transpose(self):
        for u in self.g: 
            for v in self.g[u]:
                self.g_transpose[v].append(u)

    def stronglyConnected(self):
        self.transpose()
        
        def initialize(self):
            self.visited = [False] * len(self.g)
            self.processed = [False] * len(self.g)      # used for defining compeltion of connected graph
            self.enter = [None] * len(self.g)           # kind of unneeded boiler plate
            self.exit = [None] * len(self.g)
            self.time = 0
            self.tree = []

        def dfs(self, graph, u):
            self.time +=1
            self.enter[u] = self.time
            self.visited[u] = True
            for v in graph[u]:
                if not self.visited[v]:
                    dfs(self, graph, v)
            self.time +=1
            self.processed[u] = True
            self.exit[u] = self.time
            self.tree.append(u)                 # used for appending processed nodes in a connected graph

        #1st dfs        
        initialize(self)
        for u in (self.g): 
            if not self.processed[u]: 
                dfs(self, self.g, u)
                self.tree = []                  # we really don't need this until 2nd iteration

        # 2nd dfs on first's exit times order
        second_order = []
        for i in range(len(self.g)):
            second_order.append((i, self.exit[i]))
        second_order = sorted(second_order, key = lambda x: -x[1])

        initialize(self)
        res = []                                # each res[i] is a SCC w/ nodes traversed; len(res) = # SCC's 
        for u, u_i in second_order:
            if not self.processed[u]:
                dfs(self, self.g_transpose, u)
                res.append(self.tree)           # put the traversed nodes  dfs into the res;  
                self.tree = []
        return res


# union a and b: a.union(b)
# set(list(a) + list(b))

g = Graph()

g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(1, 3)
g.addEdge(3, 4)
g.addEdge(4, 3)
g.addEdge(4, 7)
g.addEdge(3, 6)
g.addEdge(1, 5)
g.addEdge(5, 6)
g.addEdge(6, 5)
g.addEdge(6, 7)
g.addEdge(7, 7)

g.transpose()
# print([x for x in g.g])
print(g.stronglyConnected())

