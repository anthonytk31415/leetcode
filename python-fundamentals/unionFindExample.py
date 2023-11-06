


parent = [i for i in range(len(arr))]
rank = [1 for _ in range(len(arr))]

def find(u, parent): 
    if parent[u] != u: 
        find(parent[u])
    return parent[u]


def union(p_u, p_v, parent, rank):
    if rank[p_u] >= rank[p_v]:
        parent[p_v] = p_u
        rank[p_u] += rank[p_v]
    else: 
        parent[p_u] = p_v
        rank[p_v] += rank[p_u]


