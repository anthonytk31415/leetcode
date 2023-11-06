#  https://leetcode.com/problems/loud-and-rich/

from collections import defaultdict
from math import inf
from heapq import heappush, heappop

def loudAndRich(richer, quiet):
    n = len(quiet)
    res = [inf]*n

    # first, build adjacency list
    graph = defaultdict(list)
    for a, b in richer: 
        graph[a].append(b)

    # build the minheap queue 
    q = []
    for i in range(n):
        heappush(q, (quiet[i], i, i))

    visited = set()
    while q and len(visited) < n: 
        cur_quiet, quiet_idx, u = heappop(q)
        if u not in visited: 
            visited.add(u)
            if quiet[u] >= cur_quiet: 
                res[u] = quiet_idx
            for v in graph[u]:
                if v not in visited:
                    heappush(q, (cur_quiet, quiet_idx, v))
    return res

richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
quiet = [3,2,5,4,6,1,7,0]

print(loudAndRich(richer, quiet))