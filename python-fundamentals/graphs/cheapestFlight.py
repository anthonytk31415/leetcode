from collections import defaultdict
from heapq import heappush, heappop
from math import inf 
# def cheapestFlight(n, flights, src, dst, k):
#     graph = defaultdict(list)
#     for u, v, w in flights: 
#         graph[u].append([v,w])
    
#     visited = {}
#     heap = []
#     heappush(heap, (0, src, 0))         # (total dist, u, k num moves left)

#     while heap: 
#         d, u, num_moves = heappop(heap)

#         if u == dst and k >= num_moves-1: 
#             return d
#         if k < num_moves - 1: 
#             continue
#         if u not in visited or visited[u] > num_moves:
#             visited[u] = num_moves
#             for v,w in graph[u]:
#                 heappush(heap, (d + w, v, num_moves + 1))
#     return -1

# n = 4
# flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
# src = 0 
# dst = 3
# k = 1

## every time you visit, 


def cheapestFlight(n, flights, src, dst, k):
    graph = defaultdict(list)
    for u, v, w in flights: 
        graph[u].append([v,w])
    
    visited = {}
    heap = []
    heappush(heap, (0, src, k+1))         # (total dist, u, k num moves left)

    while heap: 
        d, u, num_moves = heappop(heap)
        if u == dst: 
            return d
        if num_moves ==0: 
            continue
        if u not in visited or visited[u] < num_moves:          # 
            visited[u] = num_moves
            for v,w in graph[u]:
                heappush(heap, (d + w, v, num_moves - 1))
    return -1






n = 11
flights  = [[0,3,3],[3,4,3],[4,1,3],[0,5,1],[5,1,100],[0,6,2],[6,1,100],[0,7,1],[7,8,1],[8,9,1],[9,1,1],[1,10,1],[10,2,1],[1,2,100]]
src = 0
dst = 2
k = 4
# ans = 11

print(cheapestFlight(n, flights, src, dst, k))
