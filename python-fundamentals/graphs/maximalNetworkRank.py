# maximalNetworkRank

from collections import defaultdict
from heapq import heappush, heappop


# for each road, for the pair of vertices, if their parents are not the same, union find them.

# for each vertex from 0 to n-1, count their roads, keep a 

# you need to two largest; if there are more, then select the two that do not share members of the same parent

def maximalNetworkRank2(n, roads):
    if not roads: 
        return 0

    graph = defaultdict(set)
    for u, v in roads: 
        graph[u].add(v)
        graph[v].add(u)
    
    max_roads = []
    for u in graph: 
        total_roads_u = len(graph[u])
        heappush(max_roads, (-total_roads_u, u))
    
    top_vals = []
    cur_max = None
    counter = 0
    while max_roads: 
        count_road, u = heappop(max_roads)
        count_road = -count_road
        if not cur_max: 
            cur_max = count_road
            top_vals.append([(count_road, u)])
        elif count_road == cur_max: 
            top_vals[counter].append((count_road, u))
        elif count_road < cur_max:
            counter +=1
            top_vals.append([(count_road, u)])
            cur_max = count_road

    if len(top_vals[0]) > 1: 
        candidates = set([x[1] for x in top_vals[0]])
        for u in candidates: 
            for v in candidates:
                if v == u: continue
                if v not in graph[u]: 
                    return top_vals[0][0][0]*2
        return top_vals[0][0][0]*2 - 1

    # 1 top val, possible multiple second vals; test for union
    elif len(top_vals[1]) > 1:
        candidates = set([x[1] for x in top_vals[1]])
        max_road, u = top_vals[0][0]
        for v in candidates: 
            if v not in graph[u]:
                return top_vals[1][0][0] + max_road
        return top_vals[1][0][0] + max_road - 1

    else: 
        count_0, u = top_vals[0][0]
        count_1, v = top_vals[1][0]
        if v not in graph[u]: 
            return count_0 + count_1
        else: 
            return count_0 + count_1 - 1




####### a "slower" but way cleaner, both time = O(n^2) implementation
### this one runes through all pairs
### the one above only runs throuhg the pairs of the max and 2nd max ranks

def maximalNetworkRank(n, roads):
    graph = defaultdict()
    for i in range(n):
        graph[i] = set()
    for u, v in roads: 
        graph[u].add(v)
        graph[v].add(u)

    print(graph)    
    max_rank = 0
    for u in range(n):
        for v in range(u+1, n):
            max_rank = max(max_rank, len(graph[u]) + len(graph[v]) - (u in graph[v]))
    
    return max_rank




# n = 5
# roads = [[2,3],[0,3],[0,4],[4,1]]
# ## > 4

n = 5
roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]

# n = 8
# roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]

print(maximalNetworkRank(n, roads))