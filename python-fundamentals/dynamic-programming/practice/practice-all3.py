# kruskals
from math import inf
from heapq import heappush, heappop
from bisect import bisect

def find(i, parent):
    if i != parent[i]:
        parent[i] = find(parent[i], parent)
    return parent[i]

def union(pu, pv, parent, rank):
    if rank[pu] > rank[pv]:
        parent[pv] = pu
        rank[pu] += rank[pv]
    else: 
        parent[pu] = pv
        rank[pv] += rank[pu]
        
def kruskalMST(vertices, edges):
    edges.sort(key=lambda x: x[2])
    parent = [i for i in range(vertices)]
    rank = [1 for _ in range(vertices)]
    res =  []
    e, i = 0, 0
    while e < vertices - 1: 
        u, v, w = edges[i]
        pu, pv = find(u, parent), find(v, parent)
        if pu != pv: 
            e +=1
            union(pu, pv, parent, rank)
            res.append([u,v,w])
        i += 1
    return res

edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
vertices = 4
# print(kruskalMST(vertices, edges))
# >> [[2, 3, 4], [0, 3, 5], [0, 1, 10]]


# prims
def primsMST(graph, src):
    visited = set()
    parent = [-1]*len(graph)
    distance = [inf]*len(graph)
    queue = []
    distance[src] = 0
    heappush(queue, (0, src))
    while queue: 
        cur_dist, u = heappop(queue)
        visited.add(u)
        for v in range(len(graph)):
            if v not in visited and graph[u][v] > 0 and distance[v] > graph[u][v]:
                parent[v] = u
                distance[v] = graph[u][v]
                heappush(queue, (graph[u][v], v))
    return parent, distance

graph = [[0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]

# print(primsMST(graph, 0))
# >> ([-1, 0, 1, 0, 1], [0, 2, 3, 6, 5])


# djikstras SPT
def djikstras(graph, src):
    visited = set()
    parent = [-1]*len(graph)
    distance = [inf] * len(graph)
    queue = []
    distance[src] = 0
    heappush(queue, (0, src))
    while queue: 
        cur_dist, u = heappop(queue)
        visited.add(u)
        for v in range(len(graph)):
            if v not in visited and graph[u][v] > 0 and distance[v] > graph[u][v] + cur_dist: 
                distance[v] = graph[u][v] + cur_dist
                parent[v] = u
                heappush(queue, (graph[u][v] + cur_dist, v))
    return parent, distance

graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]

# print(djikstras(graph, 0)) 
# # ([-1, 0, 1, 2, 5, 6, 7, 0, 2], [0, 4, 12, 19, 21, 11, 9, 8, 14])



# floyd warshall

def floydwarshall(graph):
    dist = [[y for y in x] for x in graph]
    for k in range(len(graph)):
        for i in range(len(graph)):
            if i == k: continue
            for j in range(len(graph)):
                if j == k: continue
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

graph = [[0, 5, inf, 10],
         [inf, 0, 3, inf],
         [inf, inf, 0,   1],
         [inf, inf, inf, 0]]

# print('first', floydwarshall(graph))
# >> [[0, 5, 8, 9], [inf, 0, 3, 4], [inf, inf, 0, 1], [inf, inf, inf, 0]]


# path lis
def path_lis(nums):
    sub, subindex, trace = [], [], [-1]*len(nums)
    for i, x in enumerate(nums):
        if not sub or x > sub[-1]:
            if subindex: 
                trace[i] = subindex[-1]
            sub.append(x)
            subindex.append(i)
        else: 
            idx = bisect(sub, x)
            if idx > 0: 
                trace[i] = subindex[idx-1]
            sub[idx] = x
            subindex[idx] = i
    path = []
    t = subindex[-1]
    while t >= 0:
        path.append(nums[t])
        t = trace[t]
    return path[::-1]

nums = [5,3,2,7,1,2,9, 10 , 0, 12]
# print(path_lis(nums))
# >> [1, 2, 9, 10, 12]

# knapsack
def knapsack(profit, weights, cap):
    profit = [0] + profit
    weights = [0] + weights
    dp = [[0] * ((cap) + 1) for w in weights]
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if j >= weights[i]:
                dp[i][j] = max(dp[i-1][j], profit[i] + dp[i][j - weights[i]])
            else : 
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1]

profit = [1, 3, 7]
weights = [1, 2, 3]
cap = 5 
# print(knapsack(profit, weights, cap))
# > 10 

# mergesort

# merge

# quicksort
def quicksort(a,p,r):
    if p >= r: 
        return 
    q = partition(a,p,r)
    quicksort(a,p,q-1)
    quicksort(a,q+1, r)


# partition
def partition(a,p,r):
    pivot = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] < pivot: 
            i +=1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i+1

a = [4,3,1,1,9,6,9,3,5]
print(quicksort(a, 0, len(a)-1 ))
print(a)

# counting sort
def countingSort(a):
    b = [0]*len(a)
    c = [0]*(max(a) + 1)
    for i in range(len(a)):
        c[a[i]] +=1
    for i in range(1, len(c)):
        c[i] = c[i] + c[i-1]
    for i in range(len(b)-1, -1, -1):
        b[c[a[i]]-1] = a[i]
        c[a[i]] -=1
    return b

# a = [4,3,1,1,9,6,9,3,5]
# print(countingSort(a))

# knapsack 