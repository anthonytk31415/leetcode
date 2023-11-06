from heapq import heappush, heappop
from math import inf 
from bisect import bisect

# kruskals MST with union find
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

def kruskal(vertices, edges):
    edges.sort(key = lambda x: x[2])
    parent = [i for i in range(vertices)]
    rank = [1 for _ in range(vertices)]
    res = []
    e, i = 0, 0
    while e < vertices - 1:
        u, v, w = edges[i]
        pu, pv = find(u, parent), find(v, parent)
        if pu != pv: 
            e +=1
            union(pu, pv, parent, rank)
            res.append([u,v,w])
        i +=1
    return res

edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
vertices = 4
# print(kruskal(vertices, edges))

# prims 
# for v times, traverse from v to u based on the smallest distance; 
def primMST(graph, src):
    visited = set()
    parent = [-1]*len(graph)
    dist =[inf]*len(graph)
    queue = []
    dist[src] = 0
    heappush(queue, (0, src))
    vertices = 0
    while vertices < len(graph): 
        dist_u, u = heappop(queue)
        visited.add(u)
        vertices +=1
        for v in range(len(graph)):
            if v not in visited and graph[u][v] > 0 and dist[v] > graph[u][v]:
                dist[v] = graph[u][v]
                parent[v] = u
                heappush(queue, (graph[u][v], v))
    return parent 
 

 

# graph = [[0, 2, 0, 6, 0],
#             [2, 0, 3, 8, 5],
#             [0, 3, 0, 0, 7],
#             [6, 8, 0, 0, 9],
#             [0, 5, 7, 9, 0]]

# print(primMST(graph, 0))
##>>  [-1, 0, 1, 0, 1]


# countingSort
def countingSort(a):
    b = [0]*len(a)
    c = [0]*(max(a)+1)
    for i in range(len(a)):
        c[a[i]] +=1
    for i in range(1, len(c)):
        c[i] = c[i] + c[i-1]
    for i in range(len(b) - 1, -1, -1):
        b[c[a[i]]-1] = a[i]
        c[a[i]] -=1
    return b


# a = [5,4,1,2,0,7,6,3]
# print(countingSort(a))

# mergesort
def mergesort(a,p,r):
    if p >= r: 
        return 
    q = (p + r) // 2
    mergesort(a,p,q)
    mergesort(a,q+1,r)
    merge(a,p,q,r)

# merge
def merge(a,p,q,r):
    left = a[p:q+1]
    right = a[q+1:r+1]
    i, j, k = 0, 0, p
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a[k] = left[i]
            i +=1
        else: 
            a[k] = right[j]
            j +=1
        k +=1
    while i < len(left):
        a[k] = left[i]
        i +=1
        k +=1
    while j < len(right):
        a[k] = right[j]
        j +=1
        k +=1

# a = [5,4,1,2,0,7,6,3]
# print(mergesort(a, 0, 7))
# print(a)

# quicksort
def quicksort(a, p, r):
    if p >= r: 
        return 
    q = partition(a,p,r)
    quicksort(a,p,q-1)
    quicksort(a,q+1,r)

# partition
def partition(a,p,r):
    pivot = a[r]
    i = p-1
    for j in range(p, r):
        if a[j] < pivot: 
            i +=1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i + 1 

# a = [5,4,1,2,0,7,6,3]
# print(quicksort(a, 0, 7))
# print(a)

# djikstras 

def djikstras(graph, src):
    visited = set()
    parent = [-1]*len(graph)
    distance = [inf]*len(graph)
    queue = []
    heappush(queue, (0, src))
    distance[src] = 0
    while queue: 
        cur_dist, u = heappop(queue)
        visited.add(u)
        for v in range(len(graph)):
            if v not in visited and graph[u][v] > 0 and distance[v] > cur_dist + graph[u][v]:
                parent[v] = u
                distance[v] = cur_dist + graph[u][v]
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

# path_lis
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
                trace[i] = subindex[idx - 1]
            sub[idx] = x
            subindex[idx] = i
    path = []
    t = subindex[-1]
    while t >= 0: 
        path.append(nums[t])
        t = trace[t]
    return path[::-1]


# nums = [5,3,2,7,1,2,9, 10 , 0, 12]
# print(path_lis(nums))
# >> [1, 2, 9, 10, 12]
# knapsack

def knapsack(profit, weights, cap):
    profit = [0] + profit
    weights = [0] + weights
    dp = [[0]*(cap + 1) for _ in weights]
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if j >= weights[i]:
                dp[i][j] = max(dp[i-1][j], profit[i] + dp[i][j - weights[i]])
            else: 
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1]

# lcm
# profit = [6, 10, 12]
# weights = [1, 2, 3]
# cap = 5
# >>30

profit = [1, 3, 7]
weights = [1, 2, 3]
cap = 5 

print(knapsack(profit, weights, cap))