from collections import defaultdict
from math import inf 

def minimumCost(source, target, original, changed, cost):
    change = defaultdict(defaultdict)
    vertices = set()
    for i in range(len(original)):
        u = original[i]
        v = changed[i]
        vertices.add(u)
        vertices.add(v)
        dist = cost[i]
        # print(u, v, dist, change)
        if change[u] and v in change[u]:
            change[u][v] = min(change[u][v], dist)
        else: 
            change[u][v] = dist

    for i in vertices: 
        for j in vertices:
            if i == j: continue
            if i != j and i not in change or j not in change[i]:
                change[i][j] = inf 

    for k in vertices:
        for i in vertices:
            for j in vertices: 
                if i != j and j != k and i != k: 
                    change[i][j] = min(change[i][j], change[i][k] + change[k][j])

    res = 0
    for i in range(len(source)):    
        u = source[i]
        v = target[i]
        if u == v: continue
        if u not in change or v not in change[u]: return -1
        if change[u][v] == inf: 
            return -1
        res += change[u][v]

    return res



# source = "abcd"
# target = "acbe"
# original = ["a","b","c","c","e","d"]
# changed = ["b","c","b","e","b","e"]
# cost = [2,5,5,1,2,20]


# source = "aaaa"
# target = "bbbb"
# original = ["a","c"]
# changed = ["c","b"]
# cost = [1,2]

source = "abcd"
target = "abce"
original = ["a"]
changed = ["e"]
cost = [10000]

print(minimumCost(source, target, original, changed, cost))