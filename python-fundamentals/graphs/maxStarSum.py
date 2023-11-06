from collections import defaultdict
from math import inf

# had the solution, but had some bugs beceause of interpretation of problem

def maxStarSum(vals, edges, k):
    graph = defaultdict(list)
    for i in range(len(vals)):
        graph[i]=list()
    for (u,v) in edges:
        if vals[v] > 0: graph[u].append(vals[v])
        if vals[u] > 0: graph[v].append(vals[u])
    for u in graph:
        # graph[u].append((u, vals[u]))
        graph[u] = sorted(graph[u], key=lambda x: -x)

    curMax = -inf
    for u in graph: 
        curStarSum = sum(graph[u][:k]) + vals[u]
        if curMax < curStarSum: 
            curMax = curStarSum
    return curMax

# vals = [1,2,3,4,10,-10,-20]
# edges = [[0,1],[1,2],[1,3],[3,4],[3,5],[3,6]]
# k = 2


# print(maxStarSum(vals, edges, k))


print(maxStarSum([-5], [], 0))

# build adjacency graph
# in adjacency graph, store tuples of vertex and value
# sort by value in descending order
# traverse all nodes and calculate the star sum in a starSum=[0]*numNodes
# keep track of max