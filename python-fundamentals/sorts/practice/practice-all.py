from bisect import bisect
from collections import deque, defaultdict
from math import inf
from heapq import heappush, heappop

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
    while t >=0:
        path.append(nums[t])
        t = trace[t]
    return path[::-1]

# nums = [3,5,7,2,1,4,9, 6, 11]
# print(path_lis(nums))


# mergesort
def mergesort(a,p,r):
    if p >= r: 
        return 
    q = (p + r) // 2
    mergesort(a, p, q)
    mergesort(a, q+1, r)
    merge(a, p, q, r)

# merge
def merge(a,p,q,r):
    left = a[p:q+1]
    right = a[q+1: r+1]
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

# a = [5,4,6,1,3,2,0,7]
# mergesort(a, 0, 7)
# print(a)
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
    i = p-1
    for j in range(p, r):
        if a[j] < pivot: 
            i +=1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i + 1

# a = [5,4,6,1,3,2,0,7]
# quicksort(a, 0, 7)
# print(a)

# countingSort

def countingSort(a):
    b = [0]*len(a)
    c = [0]*(max(a)+1)
    for i in range(len(a)):
        c[a[i]] +=1
    for i in range(1, len(c)):
        c[i] = c[i-1] + c[i]
    for i in range(len(b)-1, -1, -1):
        b[c[a[i]]-1] = a[i]
        c[a[i]] -=1
    return b

# a = [5,4,6,1,3,2,0,7]
# print(countingSort(a))


# def find
def find(i, parent):
    if i != parent[i]:
        parent[i] = find(parent[i], parent)
    return parent[i]

# def union
def union(pu, pv, parent, rank):
    if rank[pu] > rank[pv]:
        parent[pv] = pu
        rank[pu] += rank[pv]
    else: 
        parent[pu] = pv
        rank[pv] += rank[pu]

# def kruskall()
# for min spanning tree, choose smallest edges, union find them, if they have same parent, skip
def kruskall(edges, n):
    parent = [i for i in range(n)]
    rank = [1 for _ in range(n)]
    edges.sort(key=lambda x: x[2])      #edges[i] = (u,v,w)
    e, i = 0, 0
    res = []
    while e < n-1: 
        u,v,w = edges[i]
        pu, pv = find(u, parent), find(v, parent)
        if pu != pv: 
            e +=1
            union(pu, pv, parent, rank)
            res.append([u,v,w])
        i+=1
    return res

# edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
# vertices = 4
# >> [[2, 3, 4], [0, 3, 5], [0, 1, 10]]
# print(kruskall(edges, vertices))

def djikstra(graph, src):
    visited = set()
    parent = [-1] * len(graph)
    distance = [inf] * len(graph)
    heap = []
    heappush(heap, (0, src))
    distance[src] = 0
    while heap: 
        cur_dist, u = heappop(heap)
        visited.add(u)
        for v in range(len(graph)):
            ttl_dist = graph[u][v] + cur_dist
            if v not in visited and graph[u][v] > 0 and distance[v] > ttl_dist:
                distance[v] = ttl_dist
                parent[v] = u
                heappush(heap, (ttl_dist, v))
    return parent, distance

# graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
#            [4, 0, 8, 0, 0, 0, 0, 11, 0],
#            [0, 8, 0, 7, 0, 4, 0, 0, 2],
#            [0, 0, 7, 0, 9, 14, 0, 0, 0],
#            [0, 0, 0, 9, 0, 10, 0, 0, 0],
#            [0, 0, 4, 14, 10, 0, 2, 0, 0],
#            [0, 0, 0, 0, 0, 2, 0, 1, 6],
#            [8, 11, 0, 0, 0, 0, 1, 0, 7],
#            [0, 0, 2, 0, 0, 0, 6, 7, 0]
#            ]

# print(djikstra(graph, 0))

def floydwarshall(graph):
    dist = [[y for y in x] for x in graph]
    for k in range(len(graph)):
        for i in range(len(graph)):
            if i == k: continue
            for j in range(len(graph)):
                if j == k: continue
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

# graph = [[0, 5, inf, 10],
#          [inf, 0, 3, inf],
#          [inf, inf, 0,   1],
#          [inf, inf, inf, 0]]

# >> [[0, 5, 8, 9], [inf, 0, 3, 4], [inf, inf, 0, 1], [inf, inf, inf, 0]]
# print(floydwarshall(graph))

# this is for coin change
def knapsack(profit, weights, weight_cap):
    profit = [0] + profit
    weights = [0] + weights
    dp = [[0]*(weight_cap + 1) for _ in range(len(weights))]
    # i = weights number; j = weights limit 
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            print(dp)
            if i == 0 or j == 0: 
                continue
            if weights[i] <= j: 
                dp[i][j] = max(dp[i-1][j], profit[i] + dp[i][j - weights[i]])
            else: 
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1]

profit = [1, 3, 7]
weight = [1, 2, 3]
weight_cap = 5
## 22
print(knapsack(profit, weight, weight_cap))
