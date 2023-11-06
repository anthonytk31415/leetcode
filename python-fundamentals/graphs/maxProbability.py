from heapq import heappush, heappop
from math import inf
from collections import defaultdict


# Time: O(E*logV)
# Space: O(V+E)

def maxProbability(n, edges, succProb, start, end):
    probs = [-inf]*n
    graph = defaultdict(list)
    for i in range(len(edges)): 
        u, v = edges[i]
        w = succProb[i]
        graph[u].append((v, w))
        graph[v].append((u, w))
    maxHeap = [(-1, start)]      # maxHeap[i] = prob, u
    probs[start] = 1
    print(graph)


    while maxHeap:
        prob, u = heappop(maxHeap)
        prob = -prob
        print(f'popped probs: {probs}, u: {u}')
        if u == end: 
            # print(probs, u, end)
            return prob
        if probs[u] != prob: continue
        for v, w in graph[u]: 
            # print(f'u: {u}, v: {v}, succprob[v]: {succProb[v]}, prob: {prob}')
            if probs[v] < w*prob: 
                probs[v] = w*prob
                heappush(maxHeap, (-w*prob, v))
    return 0

# n = 3
# edges = [[0,1],[1,2],[0,2]]
# succProb = [0.5,0.5,0.2]
# start = 0
# end = 2

# n = 3
# edges = [[0,1],[1,2],[0,2]]
# succProb = [0.5,0.5,0.3]
# start = 0
# end = 2

n = 3
edges = [[0,1]] 
succProb = [0.5]
start = 0
end = 2

print(maxProbability(n, edges, succProb, start, end))