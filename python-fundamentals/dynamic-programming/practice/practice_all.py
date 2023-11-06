# countingsort

def countingSort(a):
    b = [None]*len(a)
    c = [0]*(max(a)+1)
    for i in range(len(a)):
        c[a[i]] +=1
    for j in range(1, len(c)):
        c[j] = c[j] + c[j-1]
    for i in range(len(b)-1, -1, -1):
        b[c[a[i]]-1] = a[i]
        c[a[i]] -=1
    return b

a = [4,3,1,1,9,6,9,3,5]
# print(countingSort(a))

# mergesort 
def mergesort(a,p,r):
    if p >= r: 
        return 
    q = (r + p)//2
    mergesort(a,p,q)
    mergesort(a,q+1,r)
    merge(a,p,q,r)

def merge(a,p,q,r):
    left = a[p:q+1]
    right = a[q+1:r+1]
    i, j = 0, 0
    k = p
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a[k] = left[i]
            i+=1
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
    
# a = [5,0,1,2,6,7,4,3]
# mergesort(a, 0, 7)
# print(a)
# quicksort

def quicksort(a, p, r):
    if p < r: 
        q = partition(a, p, r)
        quicksort(a, p, q-1)
        quicksort(a, q+1, r)

def partition(a,p,r):
    pivot = a[r]
    i = p-1
    for j in range(p, r):
        if a[j] < pivot:
            i +=1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i + 1

# a = [5,0,1,2,6,7,4,3]
# quicksort(a, 0, 7)
# print(a)

from bisect import bisect

# path_lis - path of the largest increasing subsequence
def path_lis(nums):
    sub, subindex, trace = [], [], [-1]*len(nums)
    for i, x in enumerate(nums):
        if len(sub) == 0 or x > sub[-1]:
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
    # print(subindex)
    t = subindex[-1]
    while t >= 0: 
        path.append(nums[t])
        t = trace[t]
    return path[::-1]

# nums = [5,3,2,7,1,2,9, 10 , 0, 12]
# print(path_lis(nums))
# >> [1, 2, 9, 10, 12]

# djikstras shortest path tree

from collections import deque
from heapq import heappush, heappop
from math import inf 


# graph version of djikstras
# given a graph of cost to visit and a source, return the shortest path tree
# m x m graph, m vertices

# procedure: 
# create a queue (heap), a distance array (=inf) and parent (=-1) array for each vertex (len(graph))
# add in the queue the starting src with dist = 0
# in a "while q" loop: 
# pop the minimum dist vertex; add the vertex in visited; 
# for each vertex in u, if the dist to u + weight of u/v > dist(v): add it to the queue, update the dist[v], parent[v] = u

def djikstras2(graph, src):
    queue = []
    visited = set()
    parent = [-1]*len(graph)
    heappush(queue, (0, src))
    distance = [inf]*len(graph)
    distance[src] = 0
    while queue: 
        dist, u = heappop(queue)
        visited.add(u)
        for v in range(len(graph)):
            cur_dist = dist + graph[u][v]
            if v not in visited and graph[u][v] >0 and distance[v] > cur_dist:
                parent[v] = u 
                distance[v] = cur_dist
                heappush(queue, (cur_dist, v))
    return parent, distance


def djikstras(graph, src):
    visited = set()
    distance = [inf] *len(graph)
    parent = [-1]*len(graph)
    queue = []
    distance[src] = 0
    heappush(queue, (0, src))
    while queue: 
        dist, u = heappop(queue)
        visited.add(u)
        for v in range(len(graph)):
            cur_dist = dist + graph[u][v]
            if v not in visited and graph[u][v] > 0 and distance[v] > cur_dist: 
                parent[v] = u
                distance[v] = cur_dist
                heappush(queue, (cur_dist, v))

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

# print(djikstras(graph, 0)) # ([-1, 0, 1, 2, 5, 6, 7, 0, 2], [0, 4, 12, 19, 21, 11, 9, 8, 14])

# kruskalls
# union find algorithm for a min spanning tree; 
# take the edges, sort them, 
# create the rank, find, and union functions
# then do for v -1 times, take the smallest edge, make sure they are not part of the cycle, then union find 
# when you union find, append the (u,v,w) to a res; the net end res will be the edges of a minimum spanning tree

def find(i, parent):
    if parent[i] != i: 
        return find(parent[i], parent)
    else: 
        return i

def union(p_i, p_j, parent, rank):
    if rank[p_i] > rank[p_j]:
        parent[p_j] = p_i
        rank[p_i] += rank[p_j]
    else: 
        parent[p_i] = p_j
        rank[p_j] += rank[p_i]

# vertices = num vertices, 
def kruskall(vertices, edges):
    edges.sort(key = lambda x: x[2])  ## edges = (u,v,w) where w = weight
    parent = [i for i in range(vertices)]
    rank = [1] * vertices
    res = []
    e = 0
    i = 0 
    while e < vertices - 1: 
        print(e, vertices-1)
        u, v, w = edges[i]
        print(u,v,w)
        p_u, p_v = find(u, parent), find(v, parent)
        i +=1
        if p_u != p_v: 
            union(p_u, p_v, parent, rank)
            e +=1
            res.append([u,v,w])
    return res

edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
vertices = 4
# >> [[2, 3, 4], [0, 3, 5], [0, 1, 10]]

# print(kruskall(vertices, edges))

# prims 
# find a mininum spanning tree for 

def prims(graph, src):
    parent = [-1 for i in range(len(graph))]
    distance = [inf]*len(graph)
    queue = []
    distance[src] = 0
    visited = set()
    heappush(queue, (0, src))
    while queue: 
        dist, u = heappop(queue)
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

# print(prims(graph, 0))
# >> ([-1, 0, 1, 0, 1], [0, 2, 3, 6, 5])




# floyd warshall: find shortest path from any two points on the grpah
# start with a distance graph which is a copy of the graph itself 
# then for k across all vertices, for i across all vertices, for j across all vertices: 
# if i == k: continue; if j == k: continue
# update the dist[i][j] = min of i,j and min of i,k + k,j
# return dist

def floydwarshall(graph):
    dist = [[y for y in x] for x in graph]
    n = len(graph)
    for k in range(n):
        for i in range(n):
            if i == k: continue
            for j in range(n):
                if j == k: continue
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

graph = [[0, 5, inf, 10],
         [inf, 0, 3, inf],
         [inf, inf, 0,   1],
         [inf, inf, inf, 0]]

# print('first', floydwarshall(graph))
# >> [[0, 5, 8, 9], [inf, 0, 3, 4], [inf, inf, 0, 1], [inf, inf, inf, 0]]

# nextperm


# O-1 knapsack
# maximize 
# profit[i] = profit of the jth item
# weights[j] = weights of the jth item
# limit = max weights

# can modify this with: profit[i-1] + dp[i-1][w - weights[i-1]])
# so that you can only choose the item once vs choosing an infinite amt of weight[i]'s

def knapsack(profit, weights, limit):
    dp = [[0]*(limit+1) for _ in range(len(weights)+1)]
    # print(dp)
    for i in range(1, len(dp)):
        for w in range(1, len(dp[0])):
            if w - weights[i-1] >= 0 : 
                dp[i][w] = max(dp[i-1][w], profit[i-1] + dp[i][w - weights[i-1]])
            else: 
                dp[i][w] = dp[i-1][w]

    print(dp)
    return dp[-1][-1]

# profit = [1, 3, 7]
# weight = [1, 2, 3]
# limit = 5
## 10

profit = [6, 10, 12]
weight = [1, 2, 3]
limit = 5

# >> 22


print(knapsack(profit, weight, limit))


# longest common subsequence