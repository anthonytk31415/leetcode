# Krustak's Algorithm for Min Spanning Tree (MST) 
# - return the tree that goes through all vertices with min sum of weights (via the edges)


# Properties 
# - used on undirected graphs (direted graphs are not guaranteed to be reachable from every node)
# - MST has V-1 edges for V vertices
# - output graph(s) is conneted to all vertices
#       - can be used for disconnected components but the MST will not be a single tree but multiple trees
# - MST contain no cycles 
# - Has min weights of all other spanning trees
# - Inputs are edges (order does not matter and no dupes) 
# - Greedy Algorithm
# - Needs union and find functions

# Idea: 
# - graph will be edges and weights array of arrays: [[u,v,w], [u, v, w], ...]
# - start at an arbitrary vertex 
# - instantiate: parent[i] = i for all i in vertices; mst[i] = False; rank[i] = 0; res = [] (will contain the edges of the tree)
# - indices: i = 0; e = 0; 
# - the loop: do until e =  v-1; run over all i edges but only increment e when you have a "successful" edge 
#   - a successful edge: parent of u and parent of v are not equal (note that we're taking edges that are organized by smallest, so we are taking the smallest edge to add into the set)
#   - if successful: union parent of u and parent of v; append the edge to the result

# Analysis: 
# - Time: O(ElogE), Space: O(V+E)
# - only if min heap is used for selecting a next min edge

# differences with Djikstra: 
# - returns the tree of all vertices versus returning the min path to any node

class Graph1: 
    def __init__(self, vertices) -> None:
        self.v = vertices
        self.g = []
    
    def addEdge(self, u, v, w):
        self.g.append([u,v,w])

    # find the set of an index i by cycling through parent[i] until i = parent[i]
    # the index i = the parent of the index; whe parent[i] = i; that i is the representive of that set
    def find(self, parent, i):
        if parent[i] != i:
            return self.find(parent, parent[i])
        else: 
            return parent[i]

    # Given two sets i and j (use the set representative), 
    # Union two sets by joining the smaller (by rank) set to larger
    # if equal, choose one arbitrarily and add 1 to rank
    def union(self, parent, rank, i, j ):
        if rank[i] < rank[j]:
            parent[i] = j
        elif rank[i] > rank[j]:
            parent[j] = i            
        else: 
            parent[j] = i
            rank[i] +=1

    # sort your edges by weight
    # take edges until you get V - 1 edges 
    # don't take edges if you detect a cycle
    # a cycle will be found if find(i) = find(j)

    # return min spanning tree
    def KruskalMST(self):
        #instantiate the process; i = sorting edge index; e = result index; 
        i, e, res = 0, 0, []                                # res = min spanning tree
        self.g = sorted(self.g, key = lambda x: x[2])       # sort by weight
        parent, rank = [], []        
        
        for node in range(self.v):
            parent.append(node)                                # you'll have V subsets until you start to union them based on edges
            rank.append(0)
        while e < self.v - 1:                               # take v-1 edges for MST
            u,v,w = self.g[i]
            i +=1
            p_u, p_v = self.find(parent, u), self.find(parent, v)
            if p_u != p_v:                                  # if no cycle, increment e, add that edge to res, union u and v to add to the tree
                e +=1
                res.append([u,v,w])
                self.union(parent, rank, p_u, p_v)
        
        minCost = sum([x[2] for x in res])
        print(f'returning res: {res}, minCost = {minCost}')
        return res, minCost


# class Graph: 
#     def __init__(self, vertices):
#         self.g = []
#         self.v = vertices
    
#     def addEdge(self, u, v, w):
#         self.g.append([u,v,w])

#     def find(self, parent, i):
#         if parent[i] != i:
#             return self.find(parent, parent[i])
#         else: 
#             return i

#     #takes the parents i and j; attach membership of the set to the one with the highest rank
#     def union(self, parent, rank, i, j):
#         if rank[i] > rank[j]:
#             parent[j] = i
#         elif rank[i] < rank[j]:
#             parent[i] = j
#         else: 
#             parent[j] = i
#             rank[i] +=1

#     def KruskalMST(self):
#         #instantiate:
#         parent, rank, res = [], [], []
#         i, e = 0, 0
#         self.g = sorted(self.g, key = lambda x: x[2])
#         for z in range(self.v):
#             parent.append(z)
#             rank.append(0)
#         while e < self.v - 1:
#             (u,v,w) = self.g[i]
#             print(i)
#             i +=1
#             p_u = self.find(parent, u)
#             p_v = self.find(parent, v)
#             if p_u != p_v:
#                 e +=1
#                 res.append([u,v,w])   
#                 print(res)
#                 self.union(parent, rank, p_u, p_v)
#         print(res)
#         return res



class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.g = []

    def addEdge(self, u, v, w):
        self.g.append([u,v,w])

    def find(self, parent, i):
        if parent[i] != i:
            return self.find(parent, parent[i])
        else: 
            return i

    def union(self, parent, rank, p_i, p_j):
        if rank[p_i] > rank[p_j]:
            parent[p_j] = p_i
        elif rank[p_i] < rank[p_j]:
            parent[p_i] = p_j
        else: 
            parent[p_j] = p_i
            rank[p_i] +=1

    def KruskalMST(self):
        parent, rank, res = [], [], []
        i, e = 0, 0
        self.g = sorted(self.g, key = lambda x: x[2])
        for z in range(self.v):
            parent.append(z)
            rank.append(0)
        while e < self.v - 1: 
            (u,v,w) = self.g[i]
            i +=1
            p_u = self.find(parent, u)
            p_v = self.find(parent, v)
            if p_u != p_v: 
                e +=1
                res.append([u, v, w])
                self.union(parent, rank, p_u, p_v)
        return res


#---- another rewrite ------#

class Graph1: 
    def __init__(self, vertices):
        self.g = []
        self.v = vertices

    def addEdge(self, u, v, w):
        self.g.append([u,v,w])

    def find(self, parent, i):
        if parent[i] != i:
            return self.find(parent, parent[i])
        else: 
            return i

    def union(self, parent, rank, p_i, p_j):
        if rank[p_i] > rank[p_j]:
            parent[p_j] = p_i
        elif rank[p_i] < rank[p_j]:
            parent[p_i] = p_j
        else: 
            parent[p_j] = p_i
            rank[p_i] +=1

    def KruskalMST(self):
        parent, rank, res = [], [], []
        for z in range(self.v):
            parent.append(z)
            rank.append(0)
        i = 0
        e = 0
        self.g = sorted(self.g, key = lambda x: x[2])
        while e < self.v - 1:
            u,v,w = self.g[i]
            i +=1
            p_u = self.find(parent, u)
            p_v = self.find(parent, v)
            if p_u != p_v:
                e +=1
                self.union(parent, rank, p_u, p_v)
                res.append([u,v,w])
        return res


class Graph5:
    def __init__(self, vertices):
        self.g = []
        self.v = vertices

    def addEdge(self,u,v,w):
        self.g.append([u,v,w])

    def find(self, parent, i):
        if parent[i] != i: 
            return self.find(parent, parent[i])
        else: 
            return i

    def union(self, parent, rank, p_i, p_j):
        if rank[p_i] > rank[p_j]:
            parent[p_j] = p_i
        elif rank[p_i] < rank[p_j]:
            parent[p_i] = p_j
        else: 
            rank[p_i] +=1
            parent[p_j] = p_i

    def KruskalMST(self):
        parent, rank, res = [], [], []
        i, e = 0, 0
        self.g = sorted(self.g, key = lambda x: x[2])
        for z in range(self.v):
            parent.append(z)
            rank.append(0)
        while e < self.v - 1:
            u,v,w = self.g[i]
            i +=1
            p_u = self.find(parent, u)
            p_v = self.find(parent, v)
            if p_u != p_v:
                e +=1
                self.union(parent, rank, p_u, p_v)
                res.append([u,v,w])
        return res


g = Graph5(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)
print(g.g)
# Function call
z = g.KruskalMST()
print(z)