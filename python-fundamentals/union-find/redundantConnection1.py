# straightforward union find on an undirected graph
# 

def find(parent, i):
    if parent[i] != i: 
        return find(parent, parent[i])
    else: 
        return i

def union(parent, p_i, p_j):
    parent[p_j] = p_i


def findRedundantConnection(edges):
    cycleEdge = None
    parent = []
    for i in range(len(edges)+1): # n vertices from 1 to n so leave 0th as "blank"
        parent.append(i)
    for w in edges: 
        u,v = w
        p_u = find(parent, u)
        p_v = find(parent, v)
        if p_u != p_v: 
            union(parent, p_u, p_v)
        elif p_u == p_v:
            cycleEdge = w
    return cycleEdge


edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
print(findRedundantConnection(edges))
