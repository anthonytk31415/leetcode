from math import sqrt
from collections import defaultdict

def maximumDetonation(bombs):

    graph = defaultdict(list)
    memo = [None for _ in range(len(bombs))]

    def withinExplosion(x0, y0, x1, y1, r): 
        return sqrt((x1 - x0)**2 + (y1 - y0)**2) <= r

    for i, bombI in enumerate(bombs):
        x0, y0, r0 = bombI
        for j, bombJ in enumerate(bombs):
            x1, y1, r1 = bombJ
            if i != j: 
                if withinExplosion(x0, y0, x1, y1, r0):
                    graph[i].append(j)

    def dfs(u):
        visited.add(u)
        for v in graph[u]:
            if v not in visited: dfs(v)
        return 

    for i in range(len(bombs)):
        visited = set()
        dfs(i)
        memo[i] = len(visited)

    return max(memo)

bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]

print(maximumDetonation(bombs))