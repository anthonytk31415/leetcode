# findMinHeightTrees


# - for each node: find the deepest height
# - sort the list by min
# - take the list of smallest ones

from collections import defaultdict, deque
from math import floor, ceil

class Graph:
    def __init__(self):
        self.g = defaultdict(list)
    
    def addEdge(self, u, v):
        self.g[u].append(v)
        self.g[v].append(u)

## we'll use this to traverse and then populate 

def longestPathBFS(graph, start):
    distance = {}
    parent = {}
    visited = set()
    q = deque()
    distance[start] = 0
    q.append(start)
    parent[start] = None
    maxDist = 0
    maxVertex = start
    while q:
        u = q.popleft()
        visited.add(u)
        for v in graph.g[u]:
            if v not in visited:
                q.append(v)
                parent[v] = u
                distance[v] = distance[u] + 1
                if distance[v] > maxDist:
                    maxDist = distance[v]
                    maxVertex = v
    return (maxVertex, parent)

def findPath(parent, u, v):
    res = []
    def helper(parent, u, v, res):
        res = [v] + res
        if parent[v] == None:            
            return res
        else: 
            return helper(parent, u, parent[v], res)
    return helper(parent, u,v,res)


def longestTwo(graph):
    max1_v = longestPathBFS(graph, 0)[0]
    max2 = longestPathBFS(graph, max1_v)
    (max2_v, parent) = max2

    maxPath = findPath(parent, max1_v, max2_v)

    length = len(maxPath)
    mid = length//2

    if length % 2 == 0: 
        return [maxPath[mid-1], maxPath[mid]]
    else: 
        return [maxPath[mid]]


def constructConnectedGraph(edges):
    g = Graph()
    for edge in edges:
        [u,v] = edge 
        g.addEdge(u,v)
    return g

# edges = [[1,0],[1,2],[1,3]]
# edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
edges = [[0,3],[1,3],[2,3],[4,3],[5,3],[4,6],[4,7],[5,8],[5,9]]
g = constructConnectedGraph(edges)
print(f'the graph: {g.g}')


longestPathBFS(g, 0)
z = longestTwo(g)
print(f'start: {z}')
    
# # given a single node, calculate the time
# def maxTime(node, graph):
#     status = {}
#     time  = {'time': 0}
#     for v in graph:
#         status[v] = {'enter':None, 'exit':None, 'visited': False, 'processed': False}

#     def dfs_helper(node, g, status, time):
#         time['time'] +=1
#         status[node]['enter'] = time['time']
#         status[node]['visited'] = True
#         for v in g[v]:
#             if status[v]['visited'] == False: 
#                 dfs_helper(v, g, status, time)
#         time['time'] +=1
#         status[node]['exit'] = time['time']
#         status[node]['processed'] = True

#     dfs_helper(node, graph, status, time)

#     max = 0
#     for v in graph: 
#         pass
 
# def height(node, g):
#     visited = set()
#     def helper(node, g, visited):
#         visited.add(node)
#         res = 1

#         for x in g.g[node]:
#             if x not in visited:
#                 res.append(height(x, g, visited)+1)
#         else: 
#             res.append(0)
#         return max(res)
#     return helper(node, g, visited)

# # print(height(0, g))


# # while False:
# #     print(1)
# # else: 
# #     print('hah')


# class Node: 
#     def __init__(self, val=None):
#         self.val = val
#         self.left = None
#         self.right = None

# def height(node): 
#     if not node: 
#         return 0
#     else:
#         return max(height(node.left)+1, height(node.right) + 1)

# def isBalanced(node):
#     if not node: 
#         return True
#     else:
#         return abs(height(node.right) - height(node.left)) <= 1 and isBalanced(node.right) and isBalanced(node.left)


# # root = Node(1)
# # root.left = Node(1)
# # root.left.left = Node(1)
# # root.right = Node(1)
# # root.right.right = Node(1)
# # root.right.right.right = Node(1)
# # root.right.right.right.right = Node(1)

# root = Node(1)
# root.left = Node(1)
# root.left.left = Node(1)
# root.right = Node(1)
# root.right.right = Node(1)
# root.right.right.right = Node(1)
# # root.right.right.right.right = Node(1)


# print(height(root))
# print(isBalanced(root))