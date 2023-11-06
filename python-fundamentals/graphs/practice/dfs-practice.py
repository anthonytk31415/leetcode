from collections import defaultdict, deque




class Graph: 
    def __init__(self):
        self.g = defaultdict(list)

    
    def addEdge(self, u, v):
        self.g[u].append(v)

# time complexity: visit all verteces and edges so O(V + E)
# space: O(V) since we're keeping track of the entry, exit, and times

# properties of 
# 
## DFS using while loops and a stack
def dfs(graph, start):
    visited = set()
    entry , exit, pred, time = {}, {}, {}, 0
    for v in graph.g:
        pred[v] = None
    stack = deque()
    visited.add(start)
    entry[start] = time
    time +=1
    stack.append(start) 
    curVisit = None
    while stack: 
        if not curVisit:  # remove something from stack
            curVisit = stack.pop()
        # find a child; visit the child; put parent in stack
        for v in graph.g[curVisit]: 
            if v not in visited: 
                pred[v], entry[v] = curVisit, time
                time +=1
                visited.add(v)
                stack.append(curVisit)
                curVisit = v
                break
        else:    #no more children; put curVisit = None to pop something above
            exit[curVisit] = time
            time +=1
            curVisit = None
    print(f'visited = {visited}, entry = {entry}, exit = {exit}, pred = {pred}')



## DFS using recursion

def dfsRecursion(graph, start): 
    #assign dictionaries so these variables can be mutable through the helper
    time = {'time': 0}
    visited, entry, exit, pred, = set(), {}, {}, {start: None}

    def helper(graph, start, time, visited, entry, exit, pred):
        visited.add(start)
        entry[start] = time['time']
        time['time'] +=1
        for v in graph.g[start]: 
            if v not in visited: 
                visited.add(v)
                pred[v] = start
                helper(graph, v, time, visited, entry, exit, pred)
        exit[start] = time['time']
        time['time'] +=1        
            
    helper(graph, start, time, visited, entry, exit, pred)
    print(f'visited = {visited}, entry = {entry}, exit = {exit}, pred = {pred}')





g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
# dfs(g, 0)



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
# dfs(g1, 0)

# dfsRecursion(g1, 0)
        
    # repeated step: given a node, visit an unvisited child until all are visited  
    #   - add that parent to the stack, current becomes child 
    #   - keep repeating this until you get to a node that has no children 
    # then curVisit = None
    # then you'll "backtrack": 
    # take an element from the stack, keep exploring the children 
    # once all children are visisted, then you'll backtrack

    # for times: 
    # when all children are visited, then you exit and process the time


## beware of the "legend" feature
## otherwise, 
def graphToMatrix(graph):
    dim = len(graph.g)
    matrix = [([0] * dim) for _ in range(dim)]      # create dim x dim matrix
    legend = sorted([x for x in graph.g])           # converts vertex to index of matrix in sorted order
    for i in range(len(legend)):
        v = legend[i]
        # legend[legend.index(graph.g[v])]
        for j_star in graph.g[v]:
            index = legend.index(j_star)
            j = legend[index]
            matrix[i][j] = 1
    return matrix

    # print(legend)

print(g.g)
matrix = graphToMatrix(g)
print(matrix)