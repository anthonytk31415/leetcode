# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

# dfs starting at 1. you must traverse all nodes.
# keep a visited set. 
# keep a "roads" set. every time you traverse, put the road dist in the roads set
# at the end, taxe the min of roads
# dfs until you can't dfs any more. 

from collections import defaultdict
from math import inf
def minScore(n, roads):

    graph = defaultdict(list)
    for u, v, d in roads: 
        graph[u].append((v, d))
        graph[v].append((u, d))

    def dfs(u, dist):
        visited.add(u)
        for v, d in graph[u]:
            roads.add(d)
            if v not in visited: 
                dfs(v, d)

    visited = set()
    roads = set()
    
    dfs(1, inf)
    return min(roads)

# n = 4
# roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]

n = 4
roads = [[1,2,2],[1,3,4],[3,4,7]]

n = 6
roads = [[4,5,7468],[6,2,7173],[6,3,8365],[2,3,7674],[5,6,7852],[1,2,8547],[2,4,1885],[2,5,5192],[1,3,4065],[1,4,7357]]
print(minScore(n, roads))